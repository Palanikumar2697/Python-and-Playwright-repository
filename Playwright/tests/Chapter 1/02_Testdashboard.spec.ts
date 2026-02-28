import { test, expect } from 'playwright/test'

test('Dashboard', async ({ page }) => {

    await page.goto("https://demotestivps.com/adminpaneltemplate_v2/bo/login/")
    await page.getByRole('textbox', { name: 'Username' }).fill("admin")
    await page.getByRole('textbox', { name: 'Password' }).fill("123")
    await page.getByRole('button', { name: 'Sign In' }).click()
    await expect(page).toHaveTitle('Dashboard')
    await expect(page.getByRole('link', { name: 'Logo BO Template' })).toBeVisible();
    await page.locator('#kt_app_sidebar_menu').getByRole('link', { name: ' Dashboard' }).click();
    await page.locator('#kt_app_sidebar_menu').getByRole('link', { name: ' Dashboard' }).click();
    await page.getByText('Total New Users').click();
    await expect(page.getByText('Total New Users')).toBeVisible();
    await page.getByText('Total Deposits').click();
    await page.getByText('Total Withdrawals').click();
    await page.getByText('Total ROI Earnings').click();
    await page.getByText('Total DS Earnings').click();
    await page.getByText('Total Leader Earnings').click();
    await page.getByText('Total SameLevel Earnings').click();
    await page.getByRole('heading', { name: 'Demo Wallet', exact: true }).click();
    await page.getByRole('heading', { name: 'Demo Wallet1' }).click();
    await page.getByText('Users', { exact: true }).click();
    await page.getByText('Total Users 7').click();
    await page.getByText('Blocked Users 0').click();
    await page.getByText('Under Maintenance').click();
    const page1Promise = page.waitForEvent('popup');
    await page.getByRole('link', { name: 'Demo' }).click();
    const page1 = await page1Promise;
});


