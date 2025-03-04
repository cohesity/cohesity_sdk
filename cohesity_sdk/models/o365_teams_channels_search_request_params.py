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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class O365TeamsChannelsSearchRequestParams(BaseModel):
    """
    Specifies the request parameters related to channels for Microsoft365 teams
    """ # noqa: E501
    channel_email: Optional[StrictStr] = Field(default=None, description="Specifies the email id of the channel.", alias="channelEmail")
    channel_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique id of the channel.", alias="channelId")
    channel_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the channel. Only items within the specified channel will be returned.", alias="channelName")
    include_private_channels: Optional[StrictBool] = Field(default=True, description="Specifies whether to include private channels in the response. Default is true.", alias="includePrivateChannels")
    include_public_channels: Optional[StrictBool] = Field(default=True, description="Specifies whether to include public channels in the response. Default is true.", alias="includePublicChannels")
    __properties: ClassVar[List[str]] = ["channelEmail", "channelId", "channelName", "includePrivateChannels", "includePublicChannels"]

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
        """Create an instance of O365TeamsChannelsSearchRequestParams from a JSON string"""
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
        # set to None if channel_email (nullable) is None
        # and model_fields_set contains the field
        if self.channel_email is None and "channel_email" in self.model_fields_set:
            _dict['channelEmail'] = None

        # set to None if channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.channel_id is None and "channel_id" in self.model_fields_set:
            _dict['channelId'] = None

        # set to None if channel_name (nullable) is None
        # and model_fields_set contains the field
        if self.channel_name is None and "channel_name" in self.model_fields_set:
            _dict['channelName'] = None

        # set to None if include_private_channels (nullable) is None
        # and model_fields_set contains the field
        if self.include_private_channels is None and "include_private_channels" in self.model_fields_set:
            _dict['includePrivateChannels'] = None

        # set to None if include_public_channels (nullable) is None
        # and model_fields_set contains the field
        if self.include_public_channels is None and "include_public_channels" in self.model_fields_set:
            _dict['includePublicChannels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of O365TeamsChannelsSearchRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channelEmail": obj.get("channelEmail"),
            "channelId": obj.get("channelId"),
            "channelName": obj.get("channelName"),
            "includePrivateChannels": obj.get("includePrivateChannels") if obj.get("includePrivateChannels") is not None else True,
            "includePublicChannels": obj.get("includePublicChannels") if obj.get("includePublicChannels") is not None else True
        })
        return _obj


