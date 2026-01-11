# PhysicalSourceRegistrationParams

Specifies parameters to register physical server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the physical host. | 
**applications** | **[str], none_type** | Specifies the list of applications to be registered with Physical Source. | [optional] 
**force_register** | **bool, none_type** | The agent running on a physical host will fail the registration if it is already registered as part of another cluster. By setting this option to true, agent can be forced to register with the current cluster. | [optional] 
**host_type** | **str, none_type** | Specifies the type of host. | [optional] 
**name** | **str, none_type** | A user specified human-readable name provided for the source. It contains the hostname/ip address of the physical host or the Windows Cluster VIP. | [optional] 
**physical_type** | **str, none_type** | Specifies the type of physical server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


