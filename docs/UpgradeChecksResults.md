# UpgradeChecksResults

Specifies upgrade checks results from cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_time_secs** | **int, none_type** | Specifies unix epoch finish time of checks(in seconds). | [optional] 
**node_results** | [**[UpgradeCheckNodeResult]**](UpgradeCheckNodeResult.md) | The healthcheck result for node | [optional] 
**request_type** | **str** | type of checks(preupgrade/postupgrade) | [optional] 
**result_status** | **str** | final result (running/pass/fail) of run | [optional] 
**start_time_secs** | **int, none_type** | Specifies unix epoch start time of checks(in seconds). | [optional] 
**test_run_instance_id** | **str** | Specifies test run instance of upgrade checks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


