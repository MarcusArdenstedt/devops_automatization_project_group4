# Worlkflow automation with Github action

> Project for the automation and devops course. 

This project focus on creating a workflow in github action. There are sevral job and the workflow stops if anyone fails.

## STEPS for the this project

- Create a application and check if it works localy.
- Create unit test and integration test.
- create a repository i dockerhub
- create tokens in dockerhub
- create two secrets in githhub, one for username and one for password. Value for this secrtest you get from dockerhub tokens.
- Create workflow with jobs that do differents task. one for unit testing, one for integration testing and one that build and push image to dockerhub repository.
- Use inputs with choice true or false under workflow_dispatch.
- Added a if-sats on the two jobs with testing
- When the if-sats is true and the test failed the output of that data should upload i a artifact. 

