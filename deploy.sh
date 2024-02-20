echo "switching to master"
git checkout main

echo "Deploying files to server"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/school
scp -i ~/.ssh/school -o StrictHostKeyChecking=no -r SDMS-backend ubuntu@54.236.44.210:/var/www/flask_app/
