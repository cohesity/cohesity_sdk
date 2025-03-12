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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recovery_object_identifier import RecoveryObjectIdentifier
from cohesity_sdk.cluster.models.target_teams_channel_param import TargetTeamsChannelParam
from typing import Set
from typing_extensions import Self

class TargetMsTeamParam(BaseModel):
    """
    Specifies the target Microsoft 365 Team to recover to.
    """ # noqa: E501
    parent_source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the domain during alternate domain recovery.", alias="parentSourceId")
    target_team: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="targetTeam")
    target_teams_channel_param: Optional[TargetTeamsChannelParam] = Field(default=None, alias="targetTeamsChannelParam")
    __properties: ClassVar[List[str]] = ["parentSourceId", "targetTeam", "targetTeamsChannelParam"]

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
        """Create an instance of TargetMsTeamParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target_team
        if self.target_team:
            _dict['targetTeam'] = self.target_team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_teams_channel_param
        if self.target_teams_channel_param:
            _dict['targetTeamsChannelParam'] = self.target_teams_channel_param.to_dict()
        # set to None if parent_source_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_source_id is None and "parent_source_id" in self.model_fields_set:
            _dict['parentSourceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TargetMsTeamParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parentSourceId": obj.get("parentSourceId"),
            "targetTeam": RecoveryObjectIdentifier.from_dict(obj["targetTeam"]) if obj.get("targetTeam") is not None else None,
            "targetTeamsChannelParam": TargetTeamsChannelParam.from_dict(obj["targetTeamsChannelParam"]) if obj.get("targetTeamsChannelParam") is not None else None
        })
        return _obj


