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
from cohesity_sdk.cluster.models.host_setting_check import HostSettingCheck
from typing import Optional, Set
from typing_extensions import Self

class AgentInformation(BaseModel):
    """
    Specifies the agent details.
    """ # noqa: E501
    agent_sw_version: Optional[StrictStr] = Field(default=None, description="Specifies the software version of the agent", alias="agentSwVersion")
    connection_status: Optional[StrictStr] = Field(default=None, description="Specifies the status of agent connection.", alias="connectionStatus")
    host_setting_checks: Optional[List[HostSettingCheck]] = Field(default=None, description="Specifies the list of host checks and its results.", alias="hostSettingChecks")
    last_fetched_time_in_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time in usecs when the last agent info was fetched.", alias="lastFetchedTimeInUsecs")
    support_status: Optional[StrictStr] = Field(default=None, description="Specifies the whether agent version is compatible with cluster version ro use various features.", alias="supportStatus")
    __properties: ClassVar[List[str]] = ["agentSwVersion", "connectionStatus", "hostSettingChecks", "lastFetchedTimeInUsecs", "supportStatus"]

    @field_validator('connection_status')
    def connection_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unknown', 'Healthy', 'Unregistered', 'Unreachable', 'Unhealthy', 'Error']):
            raise ValueError("must be one of enum values ('Unknown', 'Healthy', 'Unregistered', 'Unreachable', 'Unhealthy', 'Error')")
        return value

    @field_validator('support_status')
    def support_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Supported', 'Upgrade', 'Unsupported']):
            raise ValueError("must be one of enum values ('Supported', 'Upgrade', 'Unsupported')")
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
        """Create an instance of AgentInformation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in host_setting_checks (list)
        _items = []
        if self.host_setting_checks:
            for _item_host_setting_checks in self.host_setting_checks:
                if _item_host_setting_checks:
                    _items.append(_item_host_setting_checks.to_dict())
            _dict['hostSettingChecks'] = _items
        # set to None if agent_sw_version (nullable) is None
        # and model_fields_set contains the field
        if self.agent_sw_version is None and "agent_sw_version" in self.model_fields_set:
            _dict['agentSwVersion'] = None

        # set to None if connection_status (nullable) is None
        # and model_fields_set contains the field
        if self.connection_status is None and "connection_status" in self.model_fields_set:
            _dict['connectionStatus'] = None

        # set to None if host_setting_checks (nullable) is None
        # and model_fields_set contains the field
        if self.host_setting_checks is None and "host_setting_checks" in self.model_fields_set:
            _dict['hostSettingChecks'] = None

        # set to None if last_fetched_time_in_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_fetched_time_in_usecs is None and "last_fetched_time_in_usecs" in self.model_fields_set:
            _dict['lastFetchedTimeInUsecs'] = None

        # set to None if support_status (nullable) is None
        # and model_fields_set contains the field
        if self.support_status is None and "support_status" in self.model_fields_set:
            _dict['supportStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentSwVersion": obj.get("agentSwVersion"),
            "connectionStatus": obj.get("connectionStatus"),
            "hostSettingChecks": [HostSettingCheck.from_dict(_item) for _item in obj["hostSettingChecks"]] if obj.get("hostSettingChecks") is not None else None,
            "lastFetchedTimeInUsecs": obj.get("lastFetchedTimeInUsecs"),
            "supportStatus": obj.get("supportStatus")
        })
        return _obj


