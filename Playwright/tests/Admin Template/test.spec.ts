import { test, expect } from '@playwright/test';

test('Admin Login', async ({ page }) => {

  await test.step('Navigation to URL and Admin Login', async () => {
    await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login');
    await page.locator('input[name="username"]').fill('admin')
    await page.locator('input[name="password"]').fill('123')
    await page.locator('//button[@id="kt_sign_in_submit"]').click()
    

  });


  
  await test.step('User', async () => {
    
   // User List page

// Open User menu
await page.locator('span:has-text("User")').first().click();

// Open User List
await page.locator('span:has-text("User List")').first().click();

// Wait until ALL reloads + ajax finished
await page.waitForLoadState('domcontentloaded');

// Re-locate after reload (IMPORTANT)
const search = page.getByPlaceholder('Search user')

// Wait until it is really stable
await expect(search).toBeVisible({ timeout: 20000 });

// Now click
await search.click();

await search.fill('TestC002')

const row = page.locator('tr', { hasText: 'TestC002' });

const actionsBtn = row.locator('a[data-kt-menu-trigger="click"]');

await expect(actionsBtn).toBeVisible({ timeout: 10000 });
await actionsBtn.click();

// Click Actions
await page.locator('a').filter({ hasText: 'Actions' }).first().click();

// Click Edit
await page.getByRole('link', { name: 'Edit', exact: true }).click();
  });
  });
  

