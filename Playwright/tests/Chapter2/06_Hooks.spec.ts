import { test, expect } from '@playwright/test';
test('test', async ({ page }) => {
await test.step('Navigation to URL and Admin Login', async () => {
    await page.goto('https://qa.demotestivps.com/adminpaneltemplate_v2/bo/login');
    await page.getByRole('textbox',{name:'username'}).fill('admin')
    await page.getByRole('textbox',{name:'password'}).fill('123')
    await page.getByRole('button',{name:'Sign In'}).click();
});

await test.step('Dashboard', async ()=> {
  await page.locator('#kt_app_sidebar_menu').getByRole('link', { name: ' Dashboard' }).click();
  await page.getByRole('tab', { name: 'Week' }).click();
  await page.getByRole('tab', { name: 'Month' }).click();
  await page.getByRole('tab', { name: 'Today' }).click();
  await page.getByRole('button', { name: ' Filter' }).click();
  await page.getByRole('textbox', { name: 'Date From' }).click();
  await page.getByLabel('January 10,').first().click();
  await page.getByRole('textbox', { name: 'Date To' }).click();
  await page.getByLabel('January 21,').nth(1).click();
 
  await page.getByRole('button', { name: 'Apply' }).click();
});
await test.step('New Admin Creation', async () => {
      await page.locator('span:has-text("Admin")').first().click();
      await page.waitForSelector('text=Admin Lists');
      await page.locator('span:has-text("Admin Lists")').first().click()
      await page.getByText("Add New Admin").click();
      await page.getByPlaceholder("Fullname").fill("test123 ")
      await page.getByRole("textbox",{name:'username'}).fill("test123")
      await page.locator('#rpassword').fill('Admin@123')
      await page.locator('#rcpassword').fill('Admin@123')
      await page.getByPlaceholder("Email").fill("test@gmail.com")
      await page.locator("input[type='checkbox'][value='3']").click()
      await page.getByRole('button',{name:'Submit'}).click()
});
});