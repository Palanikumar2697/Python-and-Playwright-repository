import { test, expect } from '@playwright/test';

test('Capturing Screenshots', async ({ page }) => {
  await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login');
  await page.getByRole('textbox', { name: 'Username' }).click();
  await page.getByRole('textbox', { name: 'Username' }).fill('admin');
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('123');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.locator('div').filter({ hasText: 'Login Success' }).nth(1).click();
  await page
  .locator('.text-center.logo-txt.ms-2')
  .screenshot({
    path: 'tests/Screenshots/logo.png'
  });
await page
  .screenshot({
    path: 'tests/Screenshots/PageScreenshot.png'
  });
  await page
  .screenshot({
    path: 'tests/Screenshots/FullPageScreenshot.png',fullPage:true
  });
});

