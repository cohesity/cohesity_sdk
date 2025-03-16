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
from cohesity_sdk.cluster.models.m_oref import MOref
from typing import Optional, Set
from typing_extensions import Self

class VmwareStandbyObject(BaseModel):
    """
    Specifies the VMware specific standby object details.
    """ # noqa: E501
    entity_id: Optional[StrictInt] = Field(default=None, description="Specifies the entity id of the corresponding backup object for which this standby is configured.", alias="entityId")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the protection group id to which this standby object belongs.", alias="protectionGroupId")
    cdp_standby_status: Optional[StrictStr] = Field(default=None, description="Specifies the current status of the standby object protected using continuous data protection policy.", alias="CdpStandbyStatus")
    guest_id: Optional[StrictStr] = Field(default=None, description="Specifies the guest ID(OS) of the standby VM for the corresponding backup object.", alias="guestId")
    standby_m_oref: Optional[MOref] = Field(default=None, alias="standbyMOref")
    standby_time: Optional[StrictInt] = Field(default=None, description="Specifies the time till which the standby object has been hydrated for the corresponding backup object.", alias="standbyTime")
    __properties: ClassVar[List[str]] = ["entityId", "protectionGroupId", "CdpStandbyStatus", "guestId", "standbyMOref", "standbyTime"]

    @field_validator('cdp_standby_status')
    def cdp_standby_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Init', 'VMCreationInProgress', 'VMCreated', 'LogStreamingInProgress', 'ReHydrationRequired', 'ReHydrationInProgress', 'Steady', 'Disabled', 'RestoreComplete']):
            raise ValueError("must be one of enum values ('Init', 'VMCreationInProgress', 'VMCreated', 'LogStreamingInProgress', 'ReHydrationRequired', 'ReHydrationInProgress', 'Steady', 'Disabled', 'RestoreComplete')")
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
        """Create an instance of VmwareStandbyObject from a JSON string"""
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
            "protection_group_id",
            "guest_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of standby_m_oref
        if self.standby_m_oref:
            _dict['standbyMOref'] = self.standby_m_oref.to_dict()
        # set to None if entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.entity_id is None and "entity_id" in self.model_fields_set:
            _dict['entityId'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if cdp_standby_status (nullable) is None
        # and model_fields_set contains the field
        if self.cdp_standby_status is None and "cdp_standby_status" in self.model_fields_set:
            _dict['CdpStandbyStatus'] = None

        # set to None if guest_id (nullable) is None
        # and model_fields_set contains the field
        if self.guest_id is None and "guest_id" in self.model_fields_set:
            _dict['guestId'] = None

        # set to None if standby_time (nullable) is None
        # and model_fields_set contains the field
        if self.standby_time is None and "standby_time" in self.model_fields_set:
            _dict['standbyTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareStandbyObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": obj.get("entityId"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "CdpStandbyStatus": obj.get("CdpStandbyStatus"),
            "guestId": obj.get("guestId"),
            "standbyMOref": MOref.from_dict(obj["standbyMOref"]) if obj.get("standbyMOref") is not None else None,
            "standbyTime": obj.get("standbyTime")
        })
        return _obj


