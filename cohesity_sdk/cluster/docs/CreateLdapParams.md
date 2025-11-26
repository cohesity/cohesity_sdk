# CreateLdapParams

Specifies the parameters to create an LDAP.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Specifies the LDAP authentication type. | 
**base_distinguished_name** | **str, none_type** | Specifies the base distinguished name used as the base for LDAP search requests. | 
**name** | **str, none_type** | Specifies the LDAP name. | 
**active_directory_id** | **int** | Specifies the Active Directory id which is mapped to this LDAP. | [optional] 
**ad_domain_name** | **str, none_type** | Specifies the domain name of an Active Directory which is mapped to this LDAP provider | [optional] 
**attribute_common_name** | **str, none_type** | Specifies name of the LDAP attribute used for common name of an object. | [optional] 
**attribute_gid** | **str, none_type** | Specifies name of the attribute used to lookup unix GID of an LDAP user. | [optional] 
**attribute_member_of** | **str, none_type** | Specifies name of the LDAP attribute used to lookup members of a group. | [optional] 
**attribute_uid** | **str, none_type** | Specifies name of the attribute used to lookup unix UID of an LDAP user. | [optional] 
**attribute_username** | **str, none_type** | Specifies name of the LDAP attribute used to lookup a user by user ID. | [optional] 
**domain_name** | **str, none_type** | Specifies the name of the domain name to be used for querying LDAP servers from DNS. | [optional] 
**object_class_group** | **str, none_type** | Specifies name of the LDAP group object class for user accounts. | [optional] 
**object_class_user** | **str, none_type** | Specifies name of the LDAP user object class for user accounts. | [optional] 
**port** | **int, none_type** | Specifies the LDAP server port. | [optional] 
**preferred_ldap_servers** | **[str], none_type** | Specifies a list of preferred LDAP servers. Servers should either be FQDNs or IP addresses. | [optional] 
**simple_auth_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for LDAP with &#39;Simple&#39; authentication type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


