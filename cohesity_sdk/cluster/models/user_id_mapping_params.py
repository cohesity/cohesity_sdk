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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.ad_centrify_type_params import AdCentrifyTypeParams
from cohesity_sdk.cluster.models.ad_custom_attributes_type_params import AdCustomAttributesTypeParams
from cohesity_sdk.cluster.models.ad_fixed_type_params import AdFixedTypeParams
from cohesity_sdk.cluster.models.ad_ldap_provider_type_params import AdLdapProviderTypeParams
from cohesity_sdk.cluster.models.ad_nis_provider_type_params import AdNisProviderTypeParams
from cohesity_sdk.cluster.models.ad_rfc2307_type_params import AdRfc2307TypeParams
from cohesity_sdk.cluster.models.ad_sfu30_type_params import AdSfu30TypeParams
from typing import Set
from typing_extensions import Self

class UserIdMappingParams(BaseModel):
    """
    Specifies how the Unix and Windows users are mapped in an Active Directory.
    """ # noqa: E501
    centrify_type_params: Optional[AdCentrifyTypeParams] = Field(default=None, alias="centrifyTypeParams")
    custom_attributes_type_params: Optional[AdCustomAttributesTypeParams] = Field(default=None, alias="customAttributesTypeParams")
    fixed_type_params: Optional[AdFixedTypeParams] = Field(default=None, alias="fixedTypeParams")
    ldap_provider_type_params: Optional[AdLdapProviderTypeParams] = Field(default=None, alias="ldapProviderTypeParams")
    nis_provider_type_params: Optional[AdNisProviderTypeParams] = Field(default=None, alias="nisProviderTypeParams")
    rfc2307_type_params: Optional[AdRfc2307TypeParams] = Field(default=None, alias="rfc2307TypeParams")
    sfu30_type_params: Optional[AdSfu30TypeParams] = Field(default=None, alias="sfu30TypeParams")
    type: StrictStr = Field(description="Specifies the type of the mapping.")
    __properties: ClassVar[List[str]] = ["centrifyTypeParams", "customAttributesTypeParams", "fixedTypeParams", "ldapProviderTypeParams", "nisProviderTypeParams", "rfc2307TypeParams", "sfu30TypeParams", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Rfc2307', 'Sfu30', 'Centrify', 'CustomAttributes', 'LdapProvider', 'NisProvider', 'Rid', 'Fixed']):
            raise ValueError("must be one of enum values ('Rfc2307', 'Sfu30', 'Centrify', 'CustomAttributes', 'LdapProvider', 'NisProvider', 'Rid', 'Fixed')")
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
        """Create an instance of UserIdMappingParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of centrify_type_params
        if self.centrify_type_params:
            _dict['centrifyTypeParams'] = self.centrify_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_attributes_type_params
        if self.custom_attributes_type_params:
            _dict['customAttributesTypeParams'] = self.custom_attributes_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_type_params
        if self.fixed_type_params:
            _dict['fixedTypeParams'] = self.fixed_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ldap_provider_type_params
        if self.ldap_provider_type_params:
            _dict['ldapProviderTypeParams'] = self.ldap_provider_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nis_provider_type_params
        if self.nis_provider_type_params:
            _dict['nisProviderTypeParams'] = self.nis_provider_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rfc2307_type_params
        if self.rfc2307_type_params:
            _dict['rfc2307TypeParams'] = self.rfc2307_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfu30_type_params
        if self.sfu30_type_params:
            _dict['sfu30TypeParams'] = self.sfu30_type_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserIdMappingParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "centrifyTypeParams": AdCentrifyTypeParams.from_dict(obj["centrifyTypeParams"]) if obj.get("centrifyTypeParams") is not None else None,
            "customAttributesTypeParams": AdCustomAttributesTypeParams.from_dict(obj["customAttributesTypeParams"]) if obj.get("customAttributesTypeParams") is not None else None,
            "fixedTypeParams": AdFixedTypeParams.from_dict(obj["fixedTypeParams"]) if obj.get("fixedTypeParams") is not None else None,
            "ldapProviderTypeParams": AdLdapProviderTypeParams.from_dict(obj["ldapProviderTypeParams"]) if obj.get("ldapProviderTypeParams") is not None else None,
            "nisProviderTypeParams": AdNisProviderTypeParams.from_dict(obj["nisProviderTypeParams"]) if obj.get("nisProviderTypeParams") is not None else None,
            "rfc2307TypeParams": AdRfc2307TypeParams.from_dict(obj["rfc2307TypeParams"]) if obj.get("rfc2307TypeParams") is not None else None,
            "sfu30TypeParams": AdSfu30TypeParams.from_dict(obj["sfu30TypeParams"]) if obj.get("sfu30TypeParams") is not None else None,
            "type": obj.get("type")
        })
        return _obj


