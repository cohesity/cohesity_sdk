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
from cohesity_sdk.cluster.models.bgp_peer import BgpPeer
from cohesity_sdk.cluster.models.bgp_timers import BgpTimers
from typing import Set
from typing_extensions import Self

class BgpInstance(BaseModel):
    """
    BGP instance.
    """ # noqa: E501
    local_as: Optional[StrictInt] = Field(default=None, description="Local AS.", alias="localAS")
    peers: Optional[List[BgpPeer]] = Field(default=None, description="List of bgp peer groups.")
    timers: Optional[BgpTimers] = None
    __properties: ClassVar[List[str]] = ["localAS", "peers", "timers"]

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
        """Create an instance of BgpInstance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in peers (list)
        _items = []
        if self.peers:
            for _item_peers in self.peers:
                if _item_peers:
                    _items.append(_item_peers.to_dict())
            _dict['peers'] = _items
        # override the default output from pydantic by calling `to_dict()` of timers
        if self.timers:
            _dict['timers'] = self.timers.to_dict()
        # set to None if local_as (nullable) is None
        # and model_fields_set contains the field
        if self.local_as is None and "local_as" in self.model_fields_set:
            _dict['localAS'] = None

        # set to None if peers (nullable) is None
        # and model_fields_set contains the field
        if self.peers is None and "peers" in self.model_fields_set:
            _dict['peers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BgpInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "localAS": obj.get("localAS"),
            "peers": [BgpPeer.from_dict(_item) for _item in obj["peers"]] if obj.get("peers") is not None else None,
            "timers": BgpTimers.from_dict(obj["timers"]) if obj.get("timers") is not None else None
        })
        return _obj


