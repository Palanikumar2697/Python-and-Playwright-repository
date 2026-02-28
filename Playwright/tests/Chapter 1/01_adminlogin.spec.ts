import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await test.step('naviagting to url', async () => {
  await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login');
  });
  await test.step('Entering Username and Password', async () => {
  await page.getByRole('textbox', { name: 'Username' }).click();
  await page.getByRole('textbox', { name: 'Username' }).fill('admin');
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('123');
  });
  await test.step('Click on Sign In', async () => {
  await page.getByRole('button', { name: 'Sign In' }).click();
  });

  await test.step('Navigate to Dashboard of Admin Templete', async ()=> {
  await page.locator('#kt_app_sidebar_menu').getByRole('link', { name: ' Dashboard' }).click();
  await page.getByRole('tab', { name: 'Week' }).click();
  await page.getByRole('tab', { name: 'Month' }).click();
  await page.getByRole('tab', { name: 'Today' }).click();
  await page.getByRole('button', { name: ' Filter' }).click();
  await page.getByRole('textbox', { name: 'Date From' }).click();
  await page.getByLabel('January 1,').first().click();
 
  await page.getByRole('textbox', { name: 'Date To' }).click();
  await page.getByLabel('January 6,').nth(1).click();
 
  await page.getByRole('button', { name: 'Apply' }).click();
  });
  await page.getByRole('img', { name: 'user' }).click();
  await page.getByRole('link', { name: 'Sign Out' }).click();
  
});