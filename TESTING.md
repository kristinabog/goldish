[Back to README](https://github.com/kristinabog/goldish#goldish)

# Testing


## Validators

The following validators were used to make sure there were no syntax errors in the project.

[W3C HTML Validator](https://validator.w3.org/#validate_by_input)

- No errors

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

- No errors

[JSHint](https://jshint.com/)

- No errors

To test the python code, I used the built in python extension to check for PEP8 compliance
[Python testing screenshot](media/readme/python-testing.png)

- Errors in auto generated files from Django were left untouched:
    Migration files, settings.py, manage.py, checkout/init.py
- Line too long errors
    The remaining line too long errors are lines that can not be shortened without breaking the code
    

## Lighthouse Testing

All pages score in between 71% - 99%, no major issues found.

## User stories 

[View User Stories Document](media/readme/user-stories-goldish.pdf)

## Functional Testing

All pages have been tested on being responsive and passed

### Navbar and footer

| Action        | Pass/Fail  |
| ------------- |-----:|
| All navbar links redirect to the correct page  |Pass |
| All footer links redirect to the correct page  |Pass |
| Signed out, it shows the correct dropdown links when clicked on profile icon |Pass |
| Signed in, it shows the correct dropdown links when clicked on profile icon |Pass |
| The amount under the bag icon updates when adding something to your bag |Pass |
| Entering a search query, will show you results or no results |Pass |
| Footer and navbar are responsive  |Pass |


### Home
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Loading website      | Background image fades in | Pass |
| Clicking on the 'Discover now' button | Redirects you to the all products page   |  Pass |


### Products
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Hovering over a product image     | View button appears and overlay | Pass |
| Clicking on the product image | Redirects you to the product's detail page  |  Pass |
| Choosing a sorting query | Products sort by query  |  Pass |


### Product detail
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Clicking on the + and - buttons  | Quantity increments or decrements | Pass |
| Clicking on 'Add to bag' button | Adds product with the correct qty to the bag with a success toast  |  Pass |
| Clicking on 'Add to wishlist' button | Adds product to wishlist with success toast  |  Pass |
| As admin, Clicking on Edit | Redirects to form to edit product |  Pass |
| As admin, Clicking on Delete | Redirects to form modal to confirm to delete |  Pass |
| Type in review and click on 'Add review' | Review gets added with success toast |  Pass |
| Clicking on 'Edit' in your review | Refreshes page with a filled in textfield |  Pass |
| Clicking on 'Edit Review' | Review is edited with a success toast |  Pass |


### Bag
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Clicking on the + and - buttons, and then on 'update' | Quantity increments or decrements, subtotal and grand total gets updated |  Pass |
| Clicking on the 'x' icon| Product gets deleted from bag |  Pass |
| Clicking on 'Checkout' and 'Keep shopping' buttons | Redirects to the correct page |  Pass |


### Checkout 
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Loads page | Displays the correct products in the summary |  Pass |
| Filling in the form with an invalid input | form responds with error messages |  Pass |
| Checking the box for saving details to profile | delivery details are saved in profile |  Pass |
| Filling in card details | redirects to confirmation or overlay appears for bank verification  |  Pass |
| When form not submitting | Webhook created and Stripe shows 200 |  Pass |
| Successfully making an order | Redirected to confirmation page and receiving a confirmation e-mail |  Pass |


### Wishlist
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Loads page | Shows the correct products |  Pass |
| Clicking on the product picture | Redirects to product's detail page |  Pass |
| Clicking on the bin icon | Deletes product from wishlist |  Pass |


### Profile
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Changing delivery details and clicking save | Updates profile |  Pass |
| Clicking on past order number | Redirects to order's confirmation page |  Pass |

### Log In/ Register
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Fill in form on log in page | Logs you in with a toasts message |  Pass |
| Fill in register form | Makes account and shows a success message, confirmation email sent |  Pass |
| Click on confirmation link in e-mail | Redirects to page where you can click a button to confirm e-mail |  Pass |
| Logging out by clicking on log out in nav dropdown | Redirects you to a page where you can confirm you want to log out |  Pass |


### Admin
| Action     | Expected Behaviour          | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Deleting and editing products |Pass |
| Deleting and editing reviews |Pass |
| Having a 'Product management' link in profile dropdown |Pass |

## Further Testing

- The Website was tested on Google Chrome, Microsoft Edge and Firefox.

- The website was tested on all device sizes that are viewable in DevTools.

- Family members and friends were asked to test the website on their devices.

- The website was viewed on a variety of devices:

Desktop:

- HP Spectre Notebook
- Sony VAIO Fit15E (laptop)
- ASUS N73S (laptop)

Mobile:

- Samsung Galaxy A41
- Samsung Galaxy A70
- Huawei Y60 2018
- Iphone XS Max


## Bugs

- I had a lot of issues with making the webhook work when the form is not submitting. 
Even though all the code was correct and it didn't seem there were any problems, I was always receiving error 500 or 404 in Stripe.
Thanks to Tutor support, the problem was the confirmation e-mail! I accidentily switched the content in 
confirmation_email_body.txt with the content in confirmation_email_subject and this was causing the errors.

- On AWS the S3 Bucket, I had problems of my base.css not updating. Eventually I added it manually in the end.

- Unfortunately did not have the time to add error pages.

- The responsiveness of the past orders table in the profile template is a bit off on smaller screens.

