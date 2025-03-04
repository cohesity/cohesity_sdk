# Recovery

Specifies a Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_tear_down** | **bool** | Specifies whether it&#39;s possible to tear down the objects created by the recovery. | [optional] 
**creation_info** | [**CreationInfo**](CreationInfo.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**id** | **str** | Specifies the id of the Recovery. | [optional] 
**is_multi_stage_restore** | **bool** | Specifies whether the current recovery operation is a multi-stage restore operation. This is currently used by VMware recoveres for the migration/hot-standby use case. | [optional] 
**is_parent_recovery** | **bool** | Specifies whether the current recovery operation has created child recoveries. This is currently used in SQL recovery where multiple child recoveries can be tracked under a common/parent recovery. | [optional] 
**messages** | **List[str]** | Specifies messages about the recovery. | [optional] 
**name** | **str** | Specifies the name of the Recovery. | [optional] 
**parent_recovery_id** | **str** | If current recovery is child recovery triggered by another parent recovery operation, then this field willt specify the id of the parent recovery. | [optional] 
**permissions** | [**List[TenantInfo]**](TenantInfo.md) | Specifies the list of tenants that have permissions for this recovery. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for Recovery. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action. | [optional] 
**retrieve_archive_tasks** | [**List[RetrieveArchiveTask]**](RetrieveArchiveTask.md) | Specifies the list of persistent state of a retrieve of an archive task. | [optional] 
**snapshot_environment** | **str** | Specifies the type of snapshot environment for which the Recovery was performed. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**status** | **str** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the Recovery task was skipped. | [optional] 
**tear_down_message** | **str** | Specifies the error message about the tear down operation if it fails. | [optional] 
**tear_down_status** | **str** | Specifies the status of the tear down operation. This is only set when the canTearDown is set to true. &#39;DestroyScheduled&#39; indicates that the tear down is ready to schedule. &#39;Destroying&#39; indicates that the tear down is still running. &#39;Destroyed&#39; indicates that the tear down succeeded. &#39;DestroyError&#39; indicates that the tear down failed. | [optional] 
**acropolis_params** | [**RecoverAcropolisParams**](RecoverAcropolisParams.md) |  | [optional] 
**aws_params** | [**RecoverAwsParams**](RecoverAwsParams.md) |  | [optional] 
**azure_params** | [**RecoverAzureParams**](RecoverAzureParams.md) |  | [optional] 
**cassandra_params** | [**CassandraParams**](CassandraParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseParams**](CouchbaseParams.md) |  | [optional] 
**elastifile_params** | [**RecoverElastifileParams**](RecoverElastifileParams.md) |  | [optional] 
**exchange_params** | [**RecoverExchangeParams**](RecoverExchangeParams.md) |  | [optional] 
**flashblade_params** | [**RecoverFlashbladeParams**](RecoverFlashbladeParams.md) |  | [optional] 
**gcp_params** | [**RecoverGcpParams**](RecoverGcpParams.md) |  | [optional] 
**generic_nas_params** | [**RecoverGenericNasParams**](RecoverGenericNasParams.md) |  | [optional] 
**gpfs_params** | [**RecoverGpfsParams**](RecoverGpfsParams.md) |  | [optional] 
**hbase_params** | [**HbaseParams**](HbaseParams.md) |  | [optional] 
**hdfs_params** | [**HdfsParams**](HdfsParams.md) |  | [optional] 
**hive_params** | [**HiveParams**](HiveParams.md) |  | [optional] 
**hyperv_params** | [**RecoverHyperVParams**](RecoverHyperVParams.md) |  | [optional] 
**ibm_flash_system_params** | [**RecoverPureParams**](RecoverPureParams.md) |  | [optional] 
**isilon_params** | [**RecoverIsilonParams**](RecoverIsilonParams.md) |  | [optional] 
**kubernetes_params** | [**RecoverKubernetesParams**](RecoverKubernetesParams.md) |  | [optional] 
**kvm_params** | [**RecoverKvmParams**](RecoverKvmParams.md) |  | [optional] 
**mongodb_params** | [**MongodbParams**](MongodbParams.md) |  | [optional] 
**mssql_params** | [**RecoverSqlParams**](RecoverSqlParams.md) |  | [optional] 
**netapp_params** | [**RecoverNetappParams**](RecoverNetappParams.md) |  | [optional] 
**office365_params** | [**RecoverO365Params**](RecoverO365Params.md) |  | [optional] 
**oracle_params** | [**RecoverOracleParams**](RecoverOracleParams.md) |  | [optional] 
**physical_params** | [**RecoverPhysicalParams**](RecoverPhysicalParams.md) |  | [optional] 
**pure_params** | [**RecoverPureParams**](RecoverPureParams.md) |  | [optional] 
**sfdc_params** | [**RecoverSalesforceParams**](RecoverSalesforceParams.md) |  | [optional] 
**uda_params** | [**UdaParams**](UdaParams.md) |  | [optional] 
**view_params** | [**RecoverViewParams**](RecoverViewParams.md) |  | [optional] 
**vmware_params** | [**RecoverVmwareParams**](RecoverVmwareParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recovery import Recovery

# TODO update the JSON string below
json = "{}"
# create an instance of Recovery from a JSON string
recovery_instance = Recovery.from_json(json)
# print the JSON string representation of the object
print(Recovery.to_json())

# convert the object into a dict
recovery_dict = recovery_instance.to_dict()
# create an instance of Recovery from a dict
recovery_from_dict = Recovery.from_dict(recovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


