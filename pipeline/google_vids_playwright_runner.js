// Phase 5 UI runner for Antigravity/Playwright.
// This is intentionally conservative: it never stores credentials and stops on
// ambiguous/destructive UI states. Vids selectors can change, so keep selectors
// centralized here rather than scattering brittle CSS across the project.

const { chromium } = require('playwright');
const fs = require('fs');

const jobPath = process.argv[2] || 'google_vids_job.json';
const job = JSON.parse(fs.readFileSync(jobPath, 'utf8'));

const SELECTORS = {
  newVideo: /new video|create.*video/i,
  landscape: /landscape|widescreen/i,
  upload: /upload|my media/i,
  insert: /insert/i,
  preview: /preview/i,
};

async function visibleText(page, pattern) {
  return page.getByText(pattern).first();
}

async function main() {
  const context = await chromium.launchPersistentContext('.antigravity/google-profile', {
    headless: false,
    viewport: { width: 1440, height: 900 },
  });
  const page = await context.newPage();
  await page.goto('https://vids.google.com/', { waitUntil: 'domcontentloaded' });

  console.log('[Vids] Browser opened. If login is required, complete it in the visible browser.');
  await page.waitForTimeout(2500);

  // We intentionally do not auto-submit credentials or bypass security challenges.
  // The Antigravity agent may take over here if the account is not authenticated.
  await visibleText(page, SELECTORS.newVideo).click({ timeout: 15000 });
  await page.waitForTimeout(1500);

  const landscape = visibleText(page, SELECTORS.landscape);
  if (await landscape.count()) await landscape.click();

  console.log(`[Vids] Prepared ${job.objects.length} media objects.`);
  console.log('[Vids] Continue by inserting the manifest assets in order.');
  console.log('[Vids] Use object tracks for timing; use Sarvam audio as narration authority.');

  // Deliberately stop before destructive/brittle bulk clicking. Antigravity can
  // execute the generated job using the current Vids UI and capture screenshots.
  await page.screenshot({ path: 'google_vids_state.png', fullPage: true });
  await context.close();
}

main().catch(err => {
  console.error('[Vids] SAFE STOP:', err.message);
  process.exit(1);
});
