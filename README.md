# About this project

This project has the main goal to store the artifacts needed to build a blob storage triggered azure function that will add new documents to an already created index on azure AI Search.

## How to run this project locally

1. Install azure core tools
2. Create a new azure function app on vs code locally - use azure function extension
3. Change the file name `local.settings.json.template` to `local.settings.json`
4. Fill the variables on `local.settings.json` with the keys of OpenAI and Azure
5. Run the function locally and validate the execution
6. Deploy to an azure function app on azure cloud
    * Make sure you place the environment variables of `local.settings.json` into the *configuration* window on the deployed azure function app


