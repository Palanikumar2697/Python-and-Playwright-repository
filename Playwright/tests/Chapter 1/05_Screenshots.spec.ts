import { test, expect } from '@playwright/test';

test('Capturing Screenshots with Invalid credentails', async ({ page }) => {
  await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login');
  await page.getByRole('textbox', { name: 'Username' }).click();
  await page.getByRole('textbox', { name: 'Username' }).fill('admin');
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('123');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await expect(page.getByText('Admin')).toBeVisible();
  await page.getByText('Admin').click();


});