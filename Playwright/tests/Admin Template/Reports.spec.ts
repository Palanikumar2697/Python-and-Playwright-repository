import { test, expect } from '@playwright/test';

test('Admin Login', async ({ page }) => {

  await test.step('Navigation to URL and Admin Login', async () => {
    await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login');
    await page.locator('input[name="username"]').fill('admin')
    await page.locator('input[name="password"]').fill('123')
    await page.locator('//button[@id="kt_sign_in_submit"]').click()
    
  });
  

  await test.step('Reports',async () =>{
    await page.locator('span:has-text("Report")').first().click()
    await page.locator('span', { hasText: 'User Floating Wallet' }).first().click()
    await page.locator('p:has-text("Advanced Search")').click()
    await page.locator(':text-is("Select User Type")').click()
    

  });
});