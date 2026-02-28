import { test, expect } from '@playwright/test';

test('Admin Login', async ({ page }) => {

  await test.step('Navigation to URL and Admin Login', async () => {
    await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login');
    await page.locator('input[name="username"]').fill('admin')
    await page.locator('input[name="password"]').fill('123')
    await page.locator('//button[@id="kt_sign_in_submit"]').click()
    

  });

  await test.step('Verify successful login', async () => {
    // //await expect(page.locator('#kt_app_sidebar_menu')).toBeVisible()
     await expect(page.getByText('Total New Users')).toHaveText('Total New Users')
    // //await expect(page.getByTitle('Dashboard')).toBeVisible()
    

  });

  await test.step('Admin User',async ()=>{
    await page.locator('span:has-text("Admin")').first().click()
    await page.locator('span', { hasText: 'Admin Lists' }).first().click()
    await page.getByRole('button', { name: 'Add New Admin' }).click();
    await page.locator('#Fullname').fill('TestPalz');
    await page.locator('#eusername').fill('PalaniQA1');
    await page.locator('#rpassword').fill('1234');
    await page.locator('#rcpassword').fill('1234');
    await page.locator('#email').fill('mytest01@gmail.com');
    await page.locator('#checkallmem').check();
    await page.getByRole('button', { name: 'Submit' }).click();
    await page.waitForTimeout(3000)
    await page.getByPlaceholder('Search').type('PalaniQA1', { delay: 100 })
    const row = page.locator('tr', { hasText: 'PalaniQA1' });
    await page.locator('a').filter({ hasText: 'Actions' }).last().click();
    await page.locator('a').filter({ hasText: 'Edit' }).last().click()
    await page.locator('#Fullname').fill('PalzTest');
    await page.locator('#eusername').fill('QAPalani1');
    await page.locator('#rpassword').fill('1234');
    await page.locator('#rcpassword').fill('1234');
    await page.locator('#email').fill('mytest02@gmail.com');
    await page.locator('#checkallmem').check();
    await page.getByRole('button', { name: 'Submit' }).click();
  });
  
  await test.step('User', async () => {
    await page.locator('span:has-text("User")').first().click()
    await page.locator('span', { hasText: 'User List' }).first().click()
    await page.waitForLoadState('domcontentloaded');
    const search=page.getByPlaceholder('Search user')
    await expect(search).toBeVisible({ timeout: 20000 });
    await search.click()
    await search.fill('TestC002')
    const row = page.locator('tr', { hasText: 'TestC002' });
    const actionsBtn = row.locator('a[data-kt-menu-trigger="click"]');
    await expect(actionsBtn).toBeVisible({ timeout: 10000 });
    await actionsBtn.click();
    await page.locator('a').filter({ hasText: 'Actions' }).first().click();
    await page.getByRole('link', { name: 'Edit', exact: true }).click();
    await page.getByText('Add Note Status', { exact: true }).click()
    await page.locator('[name="note_status_title"]').fill('Test Status2')
    await page.locator('#note_order').selectOption({ index: 2 })
    await page.locator('#AddNewNoteStatusBtn').click()
    await page.locator('button').filter({ hasText: 'Add Note' }).last().click()
    await page.locator('[name="note_title"]').fill('New Status Test')
    // const status= page.locator("//select[@id='note_status']")
    // status.selectOption({index:1})
    // status.click()
    // const status= page.locator("//select[@id='note_status']")
    // await status.selectOption({ label: 'Test Status2' });

    // locator for dropdown (use id selector – faster & cleaner)
   const status = page.locator('#note_status');

// wait until options are loaded (safe for dynamic dropdowns)
await expect(status.locator('option')).not.toHaveCount(0);

// get only valid options (skip empty value if exists)
const options = status.locator('option:not([value=""])');
const lastIndex = (await options.count()) - 1;

// select last option
await status.selectOption({ index: lastIndex });

await page.locator("//textarea[@id='note_description']").fill('Test Description for Note Status1')
await page.locator("button[id='submitNoteBtn'] span[class='indicator-label']").click()
  });

});
    

