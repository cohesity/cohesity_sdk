# CommonApplicationServersRegistrationParams

Specifies the application servers registration config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_environments** | **[str]** | Specifies the list of application environments such as kOracle, kSQL, kExchange, kAD etc. running on the Protection Source. | 
**register_applications** | **bool, none_type** | If set to true registers application servers otherwise will update application servers registration. By default it is set to false. | [optional] 
**use_persistent_agent** | **bool, none_type** | Set to true if a persistent agent is running on the host. If this is specified, then credentials would not be used to log into the host environment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


