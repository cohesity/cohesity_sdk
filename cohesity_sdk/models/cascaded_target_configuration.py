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
from cohesity_sdk.models.targets_configuration import TargetsConfiguration
from typing import Optional, Set
from typing_extensions import Self

class CascadedTargetConfiguration(BaseModel):
    """
    Specifies the source of the cascadded replication and list of all remote targets that needs to added. Each source cluster and remote targets are considered as nodes and immediate connections between them are considered as edges.
    """ # noqa: E501
    remote_targets: TargetsConfiguration = Field(alias="remoteTargets")
    source_cluster_id: Optional[StrictInt] = Field(description="Specifies the source cluster id from where the remote operations will be performed to the next set of remote targets.", alias="sourceClusterId")
    __properties: ClassVar[List[str]] = ["remoteTargets", "sourceClusterId"]

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
        """Create an instance of CascadedTargetConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of remote_targets
        if self.remote_targets:
            _dict['remoteTargets'] = self.remote_targets.to_dict()
        # set to None if source_cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_cluster_id is None and "source_cluster_id" in self.model_fields_set:
            _dict['sourceClusterId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CascadedTargetConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "remoteTargets": TargetsConfiguration.from_dict(obj["remoteTargets"]) if obj.get("remoteTargets") is not None else None,
            "sourceClusterId": obj.get("sourceClusterId")
        })
        return _obj


