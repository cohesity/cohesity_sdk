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
from cohesity_sdk.helios.models.generic_nas_data_tiering_params import GenericNasDataTieringParams
from cohesity_sdk.helios.models.isilon_data_tiering_params import IsilonDataTieringParams
from cohesity_sdk.helios.models.netapp_data_tiering_params import NetappDataTieringParams
from typing import Set
from typing_extensions import Self

class DataTieringSource(BaseModel):
    """
    Specifies the source data tiering details.
    """ # noqa: E501
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment type of the data tiering source.")
    generic_nas_params: Optional[GenericNasDataTieringParams] = Field(default=None, alias="genericNasParams")
    isilon_params: Optional[IsilonDataTieringParams] = Field(default=None, alias="isilonParams")
    netapp_params: Optional[NetappDataTieringParams] = Field(default=None, alias="netappParams")
    __properties: ClassVar[List[str]] = ["environment", "genericNasParams", "isilonParams", "netappParams"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kGenericNas', 'kIsilon', 'kNetapp']):
            raise ValueError("must be one of enum values ('kGenericNas', 'kIsilon', 'kNetapp')")
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
        """Create an instance of DataTieringSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of generic_nas_params
        if self.generic_nas_params:
            _dict['genericNasParams'] = self.generic_nas_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_params
        if self.isilon_params:
            _dict['isilonParams'] = self.isilon_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_params
        if self.netapp_params:
            _dict['netappParams'] = self.netapp_params.to_dict()
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTieringSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environment": obj.get("environment"),
            "genericNasParams": GenericNasDataTieringParams.from_dict(obj["genericNasParams"]) if obj.get("genericNasParams") is not None else None,
            "isilonParams": IsilonDataTieringParams.from_dict(obj["isilonParams"]) if obj.get("isilonParams") is not None else None,
            "netappParams": NetappDataTieringParams.from_dict(obj["netappParams"]) if obj.get("netappParams") is not None else None
        })
        return _obj


