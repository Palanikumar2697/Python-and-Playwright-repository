import { test, expect } from '@playwright/test';

test('Admin Login', async ({ page }) => {

  await test.step('Navigation to URL and Admin Login', async () => {
    await page.goto('https://qa.demotestivps.com/adminpaneltemplate_v2/bo/login');

    await page.locator('input[name="username"]').fill('admin');
    await page.locator('input[name="password"]').fill('123');

    await page.locator("//button[@id='kt_sign_in_submit']").click()
    

  });

  await test.step('Verify successful login', async () => {
    
    await expect(page.locator('#sitename_title')).toHaveText('BO Template');

  });

  await test.step('Dashboard', async () => {

  await page.getByRole('button', { name: 'Filter' }).click();

  await page.getByRole('textbox', { name: 'Date From' }).click();
  await page.locator('div.dayContainer span').nth(0).click();

  await page.getByRole('textbox', { name: 'Date To' }).click();
  await page.locator("//div[@class='flatpickr-calendar animate open arrowTop arrowLeft']//span[@aria-label='February 2, 2026'][normalize-space()='2']").click();

  // 👉 get old value before filter
  const oldValue = await page.locator("#tot_user").innerText();

await page.locator('#filter-btn').click();

await page.waitForFunction((prev) => {
  const el = document.querySelector("#tot_user") as HTMLElement | null;
  return el && el.innerText !== prev;
}, oldValue);

  const totalUser = await page.locator("#tot_user").innerText();
  console.log("Total Users:", totalUser);

});


});
