import { test, expect } from '@playwright/test';

test('Locators Learning', async ({ page }) => {
  await page.goto('https://qa.demotestivps.com/adminpaneltemplate_v2/bo/login');

  // ---------- Login ----------
  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('123');
  await page.getByRole('button', { name: 'Sign In' }).click();

  // ---------- Dark Mode ----------
  await page.locator('#kt_header_user_menu_toggle img').hover();
  await page.getByText('Mode').click();
  await page.getByText('Dark').click();

  // ---------- System Mode ----------
  await page.locator('#kt_header_user_menu_toggle img').hover();
  await page.getByText('Mode').click();
  await page.getByText('System').click();

  // ---------- Light Mode ----------
  await page.locator('#kt_header_user_menu_toggle img').hover();
  await page.getByText('Mode').click();
  await page.getByText('Light').click();

  // ---------- Language change ----------
  await page.locator('#kt_header_user_menu_toggle img').hover();
  await page.getByText('Language').click();
  await page.getByText('简体中文').click();

  await page.locator('#kt_header_user_menu_toggle img').hover();
  await page.getByText('語言').click();
  await page.getByText('English').click();

  // ---------- Admin → Service Group ----------
  await page.getByText('Admin').click();
  await page.locator('#Admin_Service_Group').click();

  // Add Service Group
  await page.getByRole('button', { name: 'Add' }).click();
  await page.locator('#createPrivilegeGrp input').fill('Manager Access');

  await page.locator("input[value='1']").check();
  await page.locator("input[value='4']").check();
  await page.locator("input[value='5']").check();
  await page.locator("input[value='7']").check();
  await page.locator("input[value='13']").check();

  await page.getByRole('button', { name: 'Save' }).click();

  // ---------- Edit Service Group ----------
  await page.getByRole('button', { name: 'Edit' }).click();
  await page.locator('#createPrivilegeGrp input').fill('Manager Access edited');

  await page.locator("input[value='59']").check();
  await page.locator("input[value='6'][name='servicearr[]']").check();
  await page.getByRole('button', { name: 'Save' }).click();

  // ---------- View Role ----------
  await page.getByText('View Role').click();

  // ---------- Admin List ----------
  await page.getByText('Admin Lists').click();
  await page.getByRole('button', { name: 'Add New Admin' }).click();

  await page.locator('#Fullname').fill('TestQA1');
  await page.locator('#eusername').fill('AnuQA');
  await page.locator('#rpassword').fill('1234');
  await page.locator('#rcpassword').fill('1234');
  await page.locator('#email').fill('mytest@gmail.com');
  await page.locator('#checkallmem').check();

  await page.getByRole('button', { name: 'Submit' }).click();

  // ---------- Logout ----------
  await page.locator('#kt_header_user_menu_toggle img').hover();
  await page.getByText('Sign Out').click();

  // ---------- Login as new admin ----------
  await page.getByPlaceholder('Username').fill('AnuQA');
  await page.getByPlaceholder('Password').fill('1234');
  await page.getByRole('button', { name: 'Sign In' }).click();
});
