import { test, expect } from '@playwright/test';

test('Admin Login', async ({ page }) => {

  await test.step('Navigation to URL and Admin Login', async () => {
    await page.goto('https://qa.demotestivps.com/adminpaneltemplate_v2/bo/login');
    await page.locator('input[name="username"]').fill('admin');
    await page.locator('input[name="password"]').fill('123');
    await page.locator("//button[@id='kt_sign_in_submit']").click()
    

  });

  await test.step('Verify successful login', async () => {
    // await expect(page.getByText('Total New Users')).toHaveText('Total New Users');
   // await expect(page.getByText(/Total New Users/i)).toBeVisible();
   expect(page.locator('//span[text()="Total New Users"]')).toBeVisible()

  });

  await test.step('Dashboard', async ()=> {
  //await page.locator('#kt_app_sidebar_menu').getByRole('link', { name: ' Dashboard' }).click();
  await page.getByRole('button', { name: 'Filter' }).click();
  await page.getByRole('textbox', { name: 'Date From' }).click();
  await page.locator('div.dayContainer').locator('span').nth(0).click()
  await page.getByRole('textbox', { name: 'Date To' }).click();
  await page.locator("//div[@class='flatpickr-calendar animate open arrowTop arrowLeft']//span[@aria-label='February 2, 2026'][normalize-space()='2']").click();
  await page.locator('#filter-btn').click()
  page.waitForTimeout(3000)
  await page.getByRole('tab', { name: 'Week' }).click();
  page.waitForTimeout(3000)
  await page.getByRole('tab', { name: 'Month' }).click();
  page.waitForTimeout(3000)
  await page.getByRole('tab', { name: 'Today' }).click();
  page.waitForTimeout(3000)
  
});

});
