# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.simple_auth_params import SimpleAuthParams
from typing import Set
from typing_extensions import Self

class CreateLdapParams(BaseModel):
    """
    Specifies the parameters to create an LDAP.
    """ # noqa: E501
    active_directory_id: Optional[StrictInt] = Field(default=None, description="Specifies the Active Directory id which is mapped to this LDAP.", alias="activeDirectoryId")
    ad_domain_name: Optional[StrictStr] = Field(default=None, description="Specifies the domain name of an Active Directory which is mapped to this LDAP provider", alias="adDomainName")
    attribute_common_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the LDAP attribute used for common name of an object.", alias="attributeCommonName")
    attribute_gid: Optional[StrictStr] = Field(default=None, description="Specifies name of the attribute used to lookup unix GID of an LDAP user.", alias="attributeGid")
    attribute_member_of: Optional[StrictStr] = Field(default=None, description="Specifies name of the LDAP attribute used to lookup members of a group.", alias="attributeMemberOf")
    attribute_uid: Optional[StrictStr] = Field(default=None, description="Specifies name of the attribute used to lookup unix UID of an LDAP user.", alias="attributeUid")
    attribute_username: Optional[StrictStr] = Field(default=None, description="Specifies name of the LDAP attribute used to lookup a user by user ID.", alias="attributeUsername")
    auth_type: StrictStr = Field(description="Specifies the LDAP authentication type.", alias="authType")
    base_distinguished_name: Optional[StrictStr] = Field(description="Specifies the base distinguished name used as the base for LDAP search requests.", alias="baseDistinguishedName")
    domain_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the domain name to be used for querying LDAP servers from DNS.", alias="domainName")
    name: Optional[StrictStr] = Field(description="Specifies the LDAP name.")
    object_class_group: Optional[StrictStr] = Field(default=None, description="Specifies name of the LDAP group object class for user accounts.", alias="objectClassGroup")
    object_class_user: Optional[StrictStr] = Field(default=None, description="Specifies name of the LDAP user object class for user accounts.", alias="objectClassUser")
    port: Optional[StrictInt] = Field(default=None, description="Specifies the LDAP server port.")
    preferred_ldap_servers: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Specifies a list of preferred LDAP servers. Servers should either be FQDNs or IP addresses.", alias="preferredLdapServers")
    simple_auth_params: Optional[SimpleAuthParams] = Field(default=None, alias="simpleAuthParams")
    __properties: ClassVar[List[str]] = ["activeDirectoryId", "adDomainName", "attributeCommonName", "attributeGid", "attributeMemberOf", "attributeUid", "attributeUsername", "authType", "baseDistinguishedName", "domainName", "name", "objectClassGroup", "objectClassUser", "port", "preferredLdapServers", "simpleAuthParams"]

    @field_validator('auth_type')
    def auth_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Anonymous', 'Simple']):
            raise ValueError("must be one of enum values ('Anonymous', 'Simple')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateLdapParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of simple_auth_params
        if self.simple_auth_params:
            _dict['simpleAuthParams'] = self.simple_auth_params.to_dict()
        # set to None if ad_domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.ad_domain_name is None and "ad_domain_name" in self.model_fields_set:
            _dict['adDomainName'] = None

        # set to None if attribute_common_name (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_common_name is None and "attribute_common_name" in self.model_fields_set:
            _dict['attributeCommonName'] = None

        # set to None if attribute_gid (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_gid is None and "attribute_gid" in self.model_fields_set:
            _dict['attributeGid'] = None

        # set to None if attribute_member_of (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_member_of is None and "attribute_member_of" in self.model_fields_set:
            _dict['attributeMemberOf'] = None

        # set to None if attribute_uid (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_uid is None and "attribute_uid" in self.model_fields_set:
            _dict['attributeUid'] = None

        # set to None if attribute_username (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_username is None and "attribute_username" in self.model_fields_set:
            _dict['attributeUsername'] = None

        # set to None if base_distinguished_name (nullable) is None
        # and model_fields_set contains the field
        if self.base_distinguished_name is None and "base_distinguished_name" in self.model_fields_set:
            _dict['baseDistinguishedName'] = None

        # set to None if domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.domain_name is None and "domain_name" in self.model_fields_set:
            _dict['domainName'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if object_class_group (nullable) is None
        # and model_fields_set contains the field
        if self.object_class_group is None and "object_class_group" in self.model_fields_set:
            _dict['objectClassGroup'] = None

        # set to None if object_class_user (nullable) is None
        # and model_fields_set contains the field
        if self.object_class_user is None and "object_class_user" in self.model_fields_set:
            _dict['objectClassUser'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if preferred_ldap_servers (nullable) is None
        # and model_fields_set contains the field
        if self.preferred_ldap_servers is None and "preferred_ldap_servers" in self.model_fields_set:
            _dict['preferredLdapServers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateLdapParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeDirectoryId": obj.get("activeDirectoryId"),
            "adDomainName": obj.get("adDomainName"),
            "attributeCommonName": obj.get("attributeCommonName"),
            "attributeGid": obj.get("attributeGid"),
            "attributeMemberOf": obj.get("attributeMemberOf"),
            "attributeUid": obj.get("attributeUid"),
            "attributeUsername": obj.get("attributeUsername"),
            "authType": obj.get("authType"),
            "baseDistinguishedName": obj.get("baseDistinguishedName"),
            "domainName": obj.get("domainName"),
            "name": obj.get("name"),
            "objectClassGroup": obj.get("objectClassGroup"),
            "objectClassUser": obj.get("objectClassUser"),
            "port": obj.get("port"),
            "preferredLdapServers": obj.get("preferredLdapServers"),
            "simpleAuthParams": SimpleAuthParams.from_dict(obj["simpleAuthParams"]) if obj.get("simpleAuthParams") is not None else None
        })
        return _obj


