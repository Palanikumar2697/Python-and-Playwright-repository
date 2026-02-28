import { test, expect } from '@playwright/test';

test('Locators Learning', async ({ page }) => {
      await page.goto('https://qa.demotestivps.com/adminpaneltemplate_v2/bo/login');
      //Locators GetByRole
      await page.getByRole('textbox',{name:'username'}).fill('admin')
      await page.getByRole('textbox',{name:'password'}).fill('123')
      await page.getByRole('button',{name:'Sign In'}).click();
      await page.getByText('Admin').first().click()
      await page.locator('span:has-text("Admin Lists")').first().click()
      await page.getByPlaceholder('Search').type('test123', { delay: 100 })
      // const searchInput = page.getByPlaceholder('Search');
      // await searchInput.click();
      // await searchInput.type('test123', { delay: 100 });
     
      //await expect(page.getByText('test123')).toBeVisible();
     // await page.getByPlaceholder('Search').type('test123', { delay: 100 })
     
      // await page.waitForTimeout (3000);
      // await page.getByText("Add New Admin").click();
      // await page.getByPlaceholder("Fullname").fill("test123 ")
      // await page.getByRole("textbox",{name:'username'}).fill("test123")
      // await page.locator('#rpassword').fill('Admin@123')
      // await page.locator('#rcpassword').fill('Admin@123')
      // await page.getByPlaceholder("Email").fill("test@gmail.com")
      // await page.locator("input[type='checkbox'][value='3']").click()
      // await page.getByRole('button',{name:'Submit'}).click()
      //await page.locator('span:has-text("Admin Service Group")').first().click()
      


});