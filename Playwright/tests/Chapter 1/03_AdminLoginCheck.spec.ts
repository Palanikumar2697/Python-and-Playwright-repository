import { test, expect } from '@playwright/test';

test('Dashboard', async ({ page }) => {

  await test.step('Navigating to URL', async () => {
    await page.goto('https://demotestivps.com/adminpaneltemplate_v2/bo/login/');
  });

  await test.step('Enter Username and Password', async () => {
    await page.getByRole('textbox', { name: 'Username' }).fill('admin');
    await page.getByRole('textbox', { name: 'Password' }).fill('123');
  });

  await test.step('Click on Sign In Button', async () => {
    await page.getByRole('button', { name: 'Sign In' }).click();
  });

  await test.step('Assertion Checking', async () => {

    //  Assert page title
    await expect(page).toHaveTitle('Dashboard');

    const logoLink = page.getByRole('link', { name: 'Logo BO Template' });
    await expect(logoLink).toBeVisible();
    await logoLink.click();

    const userIcon = page.getByRole('img', { name: 'user' });
    await expect(userIcon).toBeVisible();
    await userIcon.click();

    
  });
});