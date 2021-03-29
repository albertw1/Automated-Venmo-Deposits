# Automated-Venmo-Deposits
This Python3 script uses an efficient method to automated Venmo deposits to your bank account. To use the Venmo API, typically you have to have a developer's account, which are no longer granted. This means you have to normally use someone's grandfathered developer credentials, which is the basis of several Github Venmo packages.

Instead, it is possible to directly log into Venmo using your web browser, then collecting the device id and associated cookies, allowing you to use the Venmo API directly. For a use case example, I have code that deposits a specified amount into your bank each month. The monthly automated deposit may be of interest to those who want a monthly scheduled ACH deposit. For example, Chase personal bankers typically suggest using Venmo as a way to satisfy a checking account's monthly ACH deposit requirement, without incurring a fee.

## Usage
1) Log into `https://www.venmo.com`. Then, input the following into your url bar, `view-source:https://venmo.com/account/settings/profile`, going to the source page of your venmo profile page.
2) Search for `"fingerprint"` and record any of the `device_id`'s found, which normally starts with `'fp01'`.
3) Input the device id you found into the Python file `venmo_automation.py` as the variable `device_id`.
4) Then, search for "bank_account" in the same source page and copy the id of the appropriate bank you wish to deposit to, setting `bank_id` to the value.
5) Input the desired amount you wish to transfer out of Venmo by setting the `total_amt` variable. $0.01 corresponds to a value of `1`, with $1.00 set as `total_amt=100`.
6) Finally, to automate this in a Linux/MacOS environment as a cronjob, open Terminal and input `crontab -e`. Using your favorite editor of choice, include a line with the time and frequency you wish to have the deposit occur. For example:

`#0 0 19 * * python3 venmo_automation.py > backup.log 2>&1`

runs the script on the 19th of each month, then appends any potential debugging output into a file name named `backup.log`.
