# UpgradecheckTestResult

Specifies an upgrade check result. Upgrade checks perform health checks on cluster before upgrade and report failures that are useful for cluster health diagnosis. When a health check executes it has one of many possible outcomes that are enumerated here. The healthcheck result can have following possible outcomes Passed - Health check has passed. Failed - Health check failed. Corrective action as described by knowledge base article for the failure must be taken to resolve failure. Skipped - Health check was skipped as it does not apply for the platform / model. Warning - Health check found issues in cluster with warning severity. diagnose the check as per knowledge base article for the check. Error - Health check execution failure. This could be due to failure for the check to be launched or unexepcted termination of the check. Timeout - Health check execution timed out.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Specifies the list of upgrade check test results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


