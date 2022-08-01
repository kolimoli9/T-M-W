"# T-M-W"
echo "# T-M-W" >> README.md
>git add README.md
>git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kolimoli9/T-M-W.git
>git push -u origin main
# Updated:
i added code to: 
* Login - added a if block to check if admin
* Home - instead of returning the book flights it will return admin page
* Airline - if block arround all of the component-cant be accessed if not airlineUser
* views.py - added to token if block to is_superuser, changed get users, changed put users, and added in post users the section that recive authorization permission.
*important to track evrey change for the correct update of the repositories.*