# OracleRangeMetaInfo

Specifies Range related information for an oracle db

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_of_range** | **int, none_type** | Specifies starting value of the range in time (usecs), SCN or sequence no. | [optional] 
**end_of_range** | **int, none_type** | Specifies ending value of the range in time (usecs), SCN or sequence no. | [optional] 
**protection_group_id** | **str, none_type** | Specifies id of the Protection Group corresponding to this oracle range | [optional] 
**reset_log_id** | **int, none_type** | Specifies resetlogs identifier associated with the oracle range. Only applicable for ranges of type SCN and sequence no. | [optional] 
**incarnation_id** | **int, none_type** | Specifies incarnation id associated with the oracle db for which the restore range belongs. Only applicable for ranges of type SCN and sequence no. | [optional] 
**thread_id** | **int, none_type** | Specifies thread id associated with the oracle db for which the restore range belongs. Only applicable for ranges of type sequence no. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


