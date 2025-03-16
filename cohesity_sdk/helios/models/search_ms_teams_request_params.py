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
from cohesity_sdk.helios.models.o365_search_request_params import O365SearchRequestParams
from cohesity_sdk.helios.models.o365_teams_channels_search_request_params import O365TeamsChannelsSearchRequestParams
from typing import Optional, Set
from typing_extensions import Self

class SearchMsTeamsRequestParams(BaseModel):
    """
    Specifies the request params to search for Teams items.
    """ # noqa: E501
    category_types: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of teams files types. Only items within the given types will be returned.", alias="categoryTypes")
    channel_names: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of channel names to filter while doing search for files.", alias="channelNames")
    channel_params: Optional[O365TeamsChannelsSearchRequestParams] = Field(default=None, alias="channelParams")
    creation_end_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in seconds when the item is created.", alias="creationEndTimeSecs")
    creation_start_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in seconds when the item is created.", alias="creationStartTimeSecs")
    o365_params: Optional[O365SearchRequestParams] = Field(default=None, alias="o365Params")
    owner_names: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of owner email ids to filter on owner of the item.", alias="ownerNames")
    search_string: Optional[StrictStr] = Field(default=None, description="Specifies the search string to filter the items. User can specify a wildcard character '*' as a suffix to a string where all item names are matched with the prefix string.", alias="searchString")
    size_bytes_lower_limit: Optional[StrictInt] = Field(default=None, description="Specifies the minimum size of the item in bytes.", alias="sizeBytesLowerLimit")
    size_bytes_upper_limit: Optional[StrictInt] = Field(default=None, description="Specifies the maximum size of the item in bytes.", alias="sizeBytesUpperLimit")
    types: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of Teams item types. Only items within the given types will be returned.")
    __properties: ClassVar[List[str]] = ["categoryTypes", "channelNames", "channelParams", "creationEndTimeSecs", "creationStartTimeSecs", "o365Params", "ownerNames", "searchString", "sizeBytesLowerLimit", "sizeBytesUpperLimit", "types"]

    @field_validator('category_types')
    def category_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Document', 'Excel', 'Powerpoint', 'Image', 'OneNote']):
                raise ValueError("each list item must be one of ('Document', 'Excel', 'Powerpoint', 'Image', 'OneNote')")
        return value

    @field_validator('types')
    def types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Channel', 'Chat', 'Conversation', 'File', 'Folder']):
                raise ValueError("each list item must be one of ('Channel', 'Chat', 'Conversation', 'File', 'Folder')")
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
        """Create an instance of SearchMsTeamsRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of channel_params
        if self.channel_params:
            _dict['channelParams'] = self.channel_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of o365_params
        if self.o365_params:
            _dict['o365Params'] = self.o365_params.to_dict()
        # set to None if category_types (nullable) is None
        # and model_fields_set contains the field
        if self.category_types is None and "category_types" in self.model_fields_set:
            _dict['categoryTypes'] = None

        # set to None if channel_names (nullable) is None
        # and model_fields_set contains the field
        if self.channel_names is None and "channel_names" in self.model_fields_set:
            _dict['channelNames'] = None

        # set to None if creation_end_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.creation_end_time_secs is None and "creation_end_time_secs" in self.model_fields_set:
            _dict['creationEndTimeSecs'] = None

        # set to None if creation_start_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.creation_start_time_secs is None and "creation_start_time_secs" in self.model_fields_set:
            _dict['creationStartTimeSecs'] = None

        # set to None if owner_names (nullable) is None
        # and model_fields_set contains the field
        if self.owner_names is None and "owner_names" in self.model_fields_set:
            _dict['ownerNames'] = None

        # set to None if search_string (nullable) is None
        # and model_fields_set contains the field
        if self.search_string is None and "search_string" in self.model_fields_set:
            _dict['searchString'] = None

        # set to None if size_bytes_lower_limit (nullable) is None
        # and model_fields_set contains the field
        if self.size_bytes_lower_limit is None and "size_bytes_lower_limit" in self.model_fields_set:
            _dict['sizeBytesLowerLimit'] = None

        # set to None if size_bytes_upper_limit (nullable) is None
        # and model_fields_set contains the field
        if self.size_bytes_upper_limit is None and "size_bytes_upper_limit" in self.model_fields_set:
            _dict['sizeBytesUpperLimit'] = None

        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchMsTeamsRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categoryTypes": obj.get("categoryTypes"),
            "channelNames": obj.get("channelNames"),
            "channelParams": O365TeamsChannelsSearchRequestParams.from_dict(obj["channelParams"]) if obj.get("channelParams") is not None else None,
            "creationEndTimeSecs": obj.get("creationEndTimeSecs"),
            "creationStartTimeSecs": obj.get("creationStartTimeSecs"),
            "o365Params": O365SearchRequestParams.from_dict(obj["o365Params"]) if obj.get("o365Params") is not None else None,
            "ownerNames": obj.get("ownerNames"),
            "searchString": obj.get("searchString"),
            "sizeBytesLowerLimit": obj.get("sizeBytesLowerLimit"),
            "sizeBytesUpperLimit": obj.get("sizeBytesUpperLimit"),
            "types": obj.get("types")
        })
        return _obj


