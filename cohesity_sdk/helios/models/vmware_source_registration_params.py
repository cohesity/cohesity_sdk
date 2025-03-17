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
from cohesity_sdk.helios.models.esxi_registration_params import EsxiRegistrationParams
from cohesity_sdk.helios.models.vcd_registration_params import VcdRegistrationParams
from cohesity_sdk.helios.models.vcenter_registration_params import VcenterRegistrationParams
from typing import Set
from typing_extensions import Self

class VmwareSourceRegistrationParams(BaseModel):
    """
    Specifies the paramaters to register a VMware source.
    """ # noqa: E501
    esxi_params: Optional[EsxiRegistrationParams] = Field(default=None, alias="esxiParams")
    type: Optional[StrictStr] = Field(description="Specifies the VMware Source type.")
    v_center_params: Optional[VcenterRegistrationParams] = Field(default=None, alias="vCenterParams")
    vcd_params: Optional[VcdRegistrationParams] = Field(default=None, alias="vcdParams")
    __properties: ClassVar[List[str]] = ["esxiParams", "type", "vCenterParams", "vcdParams"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVCenter', 'kStandaloneHost', 'kvCloudDirector']):
            raise ValueError("must be one of enum values ('kVCenter', 'kStandaloneHost', 'kvCloudDirector')")
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
        """Create an instance of VmwareSourceRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of esxi_params
        if self.esxi_params:
            _dict['esxiParams'] = self.esxi_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of v_center_params
        if self.v_center_params:
            _dict['vCenterParams'] = self.v_center_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vcd_params
        if self.vcd_params:
            _dict['vcdParams'] = self.vcd_params.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareSourceRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "esxiParams": EsxiRegistrationParams.from_dict(obj["esxiParams"]) if obj.get("esxiParams") is not None else None,
            "type": obj.get("type"),
            "vCenterParams": VcenterRegistrationParams.from_dict(obj["vCenterParams"]) if obj.get("vCenterParams") is not None else None,
            "vcdParams": VcdRegistrationParams.from_dict(obj["vcdParams"]) if obj.get("vcdParams") is not None else None
        })
        return _obj


