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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ViewFailover(BaseModel):
    """
    Specifies the failover status of a view.
    """ # noqa: E501
    is_failover_ready: Optional[StrictBool] = Field(default=None, description="Specifies if the view is ready for failover.", alias="isFailoverReady")
    remote_cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the remote cluster id.", alias="remoteClusterId")
    remote_cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies the remote cluster incarnation id.", alias="remoteClusterIncarnationId")
    remote_view_id: Optional[StrictInt] = Field(default=None, description="Specifies the remote view id.", alias="remoteViewId")
    view_uid: Optional[StrictStr] = Field(default=None, description="View uid.", alias="viewUid")
    __properties: ClassVar[List[str]] = ["isFailoverReady", "remoteClusterId", "remoteClusterIncarnationId", "remoteViewId", "viewUid"]

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
        """Create an instance of ViewFailover from a JSON string"""
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
        # set to None if is_failover_ready (nullable) is None
        # and model_fields_set contains the field
        if self.is_failover_ready is None and "is_failover_ready" in self.model_fields_set:
            _dict['isFailoverReady'] = None

        # set to None if remote_cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_cluster_id is None and "remote_cluster_id" in self.model_fields_set:
            _dict['remoteClusterId'] = None

        # set to None if remote_cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_cluster_incarnation_id is None and "remote_cluster_incarnation_id" in self.model_fields_set:
            _dict['remoteClusterIncarnationId'] = None

        # set to None if remote_view_id (nullable) is None
        # and model_fields_set contains the field
        if self.remote_view_id is None and "remote_view_id" in self.model_fields_set:
            _dict['remoteViewId'] = None

        # set to None if view_uid (nullable) is None
        # and model_fields_set contains the field
        if self.view_uid is None and "view_uid" in self.model_fields_set:
            _dict['viewUid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewFailover from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isFailoverReady": obj.get("isFailoverReady"),
            "remoteClusterId": obj.get("remoteClusterId"),
            "remoteClusterIncarnationId": obj.get("remoteClusterIncarnationId"),
            "remoteViewId": obj.get("remoteViewId"),
            "viewUid": obj.get("viewUid")
        })
        return _obj


