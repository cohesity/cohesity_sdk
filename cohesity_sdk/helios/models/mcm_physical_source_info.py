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
from cohesity_sdk.helios.models.mcm_agent_info import McmAgentInfo
from typing import Set
from typing_extensions import Self

class McmPhysicalSourceInfo(BaseModel):
    """
    Specifies the information for a physical source.
    """ # noqa: E501
    agents_info: Optional[List[McmAgentInfo]] = Field(default=None, description="Specifies the information for agents related to source.", alias="agentsInfo")
    host_type: Optional[StrictStr] = Field(default=None, description="Specifies the operating system of the physical host.", alias="hostType")
    upgradability: Optional[StrictStr] = Field(default=None, description="Specifies the upgradability of the agent software.")
    upgrade_error: Optional[StrictStr] = Field(default=None, description="Specifies the upgrade error if any for the agent.", alias="upgradeError")
    upgrade_status: Optional[StrictStr] = Field(default=None, description="Specifies the current upgrade status of the agent.", alias="upgradeStatus")
    __properties: ClassVar[List[str]] = ["agentsInfo", "hostType", "upgradability", "upgradeError", "upgradeStatus"]

    @field_validator('host_type')
    def host_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kLinux', 'kWindows', 'kAix', 'kSolaris', 'kSapHana', 'kOther', 'kHPUX', 'kVOS']):
            raise ValueError("must be one of enum values ('kLinux', 'kWindows', 'kAix', 'kSolaris', 'kSapHana', 'kOther', 'kHPUX', 'kVOS')")
        return value

    @field_validator('upgradability')
    def upgradability_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Upgradable', 'Current', 'Unknown', 'NonUpgradableInvalidVersion', 'NonUpgradableAgentIsNewer', 'NonUpgradableAgentIsOld']):
            raise ValueError("must be one of enum values ('Upgradable', 'Current', 'Unknown', 'NonUpgradableInvalidVersion', 'NonUpgradableAgentIsNewer', 'NonUpgradableAgentIsOld')")
        return value

    @field_validator('upgrade_status')
    def upgrade_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Idle', 'Accepted', 'Started', 'Finished', 'Scheduled']):
            raise ValueError("must be one of enum values ('Idle', 'Accepted', 'Started', 'Finished', 'Scheduled')")
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
        """Create an instance of McmPhysicalSourceInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in agents_info (list)
        _items = []
        if self.agents_info:
            for _item_agents_info in self.agents_info:
                if _item_agents_info:
                    _items.append(_item_agents_info.to_dict())
            _dict['agentsInfo'] = _items
        # set to None if host_type (nullable) is None
        # and model_fields_set contains the field
        if self.host_type is None and "host_type" in self.model_fields_set:
            _dict['hostType'] = None

        # set to None if upgradability (nullable) is None
        # and model_fields_set contains the field
        if self.upgradability is None and "upgradability" in self.model_fields_set:
            _dict['upgradability'] = None

        # set to None if upgrade_error (nullable) is None
        # and model_fields_set contains the field
        if self.upgrade_error is None and "upgrade_error" in self.model_fields_set:
            _dict['upgradeError'] = None

        # set to None if upgrade_status (nullable) is None
        # and model_fields_set contains the field
        if self.upgrade_status is None and "upgrade_status" in self.model_fields_set:
            _dict['upgradeStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of McmPhysicalSourceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentsInfo": [McmAgentInfo.from_dict(_item) for _item in obj["agentsInfo"]] if obj.get("agentsInfo") is not None else None,
            "hostType": obj.get("hostType"),
            "upgradability": obj.get("upgradability"),
            "upgradeError": obj.get("upgradeError"),
            "upgradeStatus": obj.get("upgradeStatus")
        })
        return _obj


