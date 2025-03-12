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
from cohesity_sdk.helios.models.fallback_user_id_mapping_params import FallbackUserIdMappingParams
from typing import Optional, Set
from typing_extensions import Self

class AdCentrifyTypeParams(BaseModel):
    """
    Specifies the properties associated to a Centrify type user id mapping.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(description="Specifies a description of the Centrify zone.")
    distinguished_name: Optional[StrictStr] = Field(description="Specifies the distinguished name of the Centrify zone.", alias="distinguishedName")
    var_schema: Optional[StrictStr] = Field(description="Specifies the schema of this Centrify zone.", alias="schema")
    zone_domain: Optional[StrictStr] = Field(default=None, description="Specifies the zone domain of the Centrify zone.", alias="zoneDomain")
    zone_name: Optional[StrictStr] = Field(default=None, description="Specifies the zone name of the Centrify zone.", alias="zoneName")
    fallback_option: FallbackUserIdMappingParams = Field(alias="fallbackOption")
    __properties: ClassVar[List[str]] = ["description", "distinguishedName", "schema", "zoneDomain", "zoneName", "fallbackOption"]

    @field_validator('var_schema')
    def var_schema_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CentrifyDynamicSchema_1_0', 'CentrifyDynamicSchema_2_0', 'CentrifySfu_3_0', 'CentrifySfu_4_0', 'CentrifyCdcRfc2307', 'CentrifyDynamicSchema_3_0', 'CentrifyCdcRfc2307_2', 'CentrifyDynamicSchema_5_0', 'CentrifyCdcRfc2307_3', 'CentrifySfu_3_0_V5']):
            raise ValueError("must be one of enum values ('CentrifyDynamicSchema_1_0', 'CentrifyDynamicSchema_2_0', 'CentrifySfu_3_0', 'CentrifySfu_4_0', 'CentrifyCdcRfc2307', 'CentrifyDynamicSchema_3_0', 'CentrifyCdcRfc2307_2', 'CentrifyDynamicSchema_5_0', 'CentrifyCdcRfc2307_3', 'CentrifySfu_3_0_V5')")
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
        """Create an instance of AdCentrifyTypeParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "zone_domain",
            "zone_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of fallback_option
        if self.fallback_option:
            _dict['fallbackOption'] = self.fallback_option.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if distinguished_name (nullable) is None
        # and model_fields_set contains the field
        if self.distinguished_name is None and "distinguished_name" in self.model_fields_set:
            _dict['distinguishedName'] = None

        # set to None if var_schema (nullable) is None
        # and model_fields_set contains the field
        if self.var_schema is None and "var_schema" in self.model_fields_set:
            _dict['schema'] = None

        # set to None if zone_domain (nullable) is None
        # and model_fields_set contains the field
        if self.zone_domain is None and "zone_domain" in self.model_fields_set:
            _dict['zoneDomain'] = None

        # set to None if zone_name (nullable) is None
        # and model_fields_set contains the field
        if self.zone_name is None and "zone_name" in self.model_fields_set:
            _dict['zoneName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdCentrifyTypeParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "distinguishedName": obj.get("distinguishedName"),
            "schema": obj.get("schema"),
            "zoneDomain": obj.get("zoneDomain"),
            "zoneName": obj.get("zoneName"),
            "fallbackOption": FallbackUserIdMappingParams.from_dict(obj["fallbackOption"]) if obj.get("fallbackOption") is not None else None
        })
        return _obj


