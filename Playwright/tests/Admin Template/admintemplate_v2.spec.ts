import { test, expect } from '@playwright/test';

test('Admin Login', async ({ page }) => {
await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login/');
await page.getByRole('textbox', { name: 'Username' }).click();
await page.getByRole('textbox', { name: 'Username' }).fill('admin');
await page.getByRole('textbox', { name: 'Password' }).click();
await page.getByRole('textbox', { name: 'Password' }).fill('123');
await page.getByRole('button', { name: 'Sign In' }).click();
await page.getByRole('link', { name: 'Logo BO Template' }).click();
await page.getByRole('img', { name: 'user' }).click();
await page.getByRole('link', { name: 'Account Settings' }).click();
await page.getByRole('link', { name: 'Settings' }).click();
await page.getByRole('link', { name: 'Home' }).click();
await page.getByRole('button', { name: ' Filter' }).click();
await page.getByRole('textbox', { name: 'Date From' }).click();
await page.getByLabel('February 1,').first().click();
await page.getByRole('textbox', { name: 'Date From' }).fill('01-02-2026');
await page.getByRole('textbox', { name: 'Date To' }).click();
await page.getByLabel('February 3,').nth(1).click();
await page.getByRole('textbox', { name: 'Date To' }).fill('03-02-2026');
await page.getByRole('button', { name: 'Apply' }).click();
await page.getByRole('button', { name: ' Filter' }).click();
await page.getByRole('button', { name: 'Reset' }).click();
await page.getByRole('tab', { name: 'Today' }).click();
await page.getByRole('tab', { name: 'Week' }).click();
await page.getByRole('tab', { name: 'Month' }).click();
await page.locator('#refreshButton').click();
await page.getByRole('row', { name: 'Under Maintenance' }).locator('label').click();
await page.getByRole('button', { name: 'Yes' }).click();
await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/');
await page.locator('#kt_app_sidebar_menu').getByRole('link', { name: ' AI Earning Dashboard' }).click();
await page.locator('.ki-outline.ki-arrow-up').click();

});