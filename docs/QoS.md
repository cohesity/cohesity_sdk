# QoS

Specifies the Quality of Service (QoS) Policy for the View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the QoS Policy. If not specified, the default is &#39;BackupTargetLow&#39;.  BackupTargetAuto: (Applicable only for C6K Platform) Use this policy for workloads such as backups, which keep many I/Os outstanding. This policy splits I/Os across SSDs and HDDs to achieve maximum performance based on the current usage. The priority for processing workload with this policy is the same as Backup Target High and Backup Target SSD.  JournaledSequentialDump: Use this policy for workloads that write large amounts of data sequentially to a very small number of files and do not keep many I/Os outstanding. By default data is written to the SSD and has the highest priority and low latency.  TestAndDevHigh: Use this policy for workloads that require lower I/O latency or do not keep many I/Os outstanding, as the I/Os are given higher priority compared to other QoS policies. Data is written to the SSD.  TestAndDevLow: The same as TestAndDev High, except that the I/Os with this QoS policy are given lower priority compared to I/Os with TestAndDev High when there is contention.  BackupTargetCommvault: Use this policy to intelligently detect and exclude application-specific markers to achieve better deduplication when CommVault backup application is writing to a Cohesity View. Data is written to SSD and has the same priority and latency as TestAndDev High.  BackupTargetSSD: Use this policy for workloads such as backups, which keep many I/Os outstanding, but in this case, DataPlatform sends both sequential and random I/Os to SSD. The latency is lower than other Backup Target policies. The priority for processing workload with this policy is the same as Backup Target Auto.  BackupTargetHigh: Use this policy for non-latency sensitive workloads such as backups, which keep many I/Os outstanding. Data is written to HDD and has higher latency compared to other QoS policies writing to a SSD The priority for processing workload with this policy is the same as Backup Target Auto.  BackupTargetLow: The same as Backup Target High, except that the priority for processing workloads with this policy is lower than workloads with Backup Target Auto / High /SSD when there is contention. | [optional] 
**principal_id** | **int** | Specifies the id of the QoS Policy used for the View. (Deprecated) This parameter is deprecated and shall not be supported in future releases. Use name instead. | [optional] 
**principal_name** | **str** | Specifies the name of the QoS Policy. If not specified, the default is &#39;Backup Target Low&#39;. (To be deprecated in future release, use name instead) | [optional] 

## Example

```python
from cohesity_sdk.models.qo_s import QoS

# TODO update the JSON string below
json = "{}"
# create an instance of QoS from a JSON string
qo_s_instance = QoS.from_json(json)
# print the JSON string representation of the object
print(QoS.to_json())

# convert the object into a dict
qo_s_dict = qo_s_instance.to_dict()
# create an instance of QoS from a dict
qo_s_from_dict = QoS.from_dict(qo_s_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


