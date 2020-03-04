# Deploy trained model from `JerryCompletes` in Google Cloud Platform:

* Download and install Cloud SDK https://cloud.google.com/sdk/docs
* Create a new project:

`gcloud projects create [YOUR_PROJECT_ID] --set-as-default`

* Initialize your App Engine app with your project

`gcloud app create --project=[YOUR_PROJECT_ID]`

* `cd` into `DeployJerry` and deploy to the App Engine standard environment (make sure trained model is in `model` dir)

`gcloud app deploy`

* Launch your browser to view the app at `https://PROJECT_ID.appspot.com`

`gcloud app browse`
