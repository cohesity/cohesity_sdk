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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.file_count import FileCount
from cohesity_sdk.cluster.models.files_stats_for_entity import FilesStatsForEntity
from typing import Set
from typing_extensions import Self

class FilesStats(BaseModel):
    """
    Specifies the files stats.
    """ # noqa: E501
    file_size_distribution: Optional[List[FileCount]] = Field(default=None, description="Specifies the aggregated distribution by size of files stored in the Cohesity cluster.", alias="fileSizeDistribution")
    files_stats: Optional[List[FilesStatsForEntity]] = Field(default=None, description="Specifies a list of file stats for entities.", alias="filesStats")
    __properties: ClassVar[List[str]] = ["fileSizeDistribution", "filesStats"]

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
        """Create an instance of FilesStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in file_size_distribution (list)
        _items = []
        if self.file_size_distribution:
            for _item_file_size_distribution in self.file_size_distribution:
                if _item_file_size_distribution:
                    _items.append(_item_file_size_distribution.to_dict())
            _dict['fileSizeDistribution'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in files_stats (list)
        _items = []
        if self.files_stats:
            for _item_files_stats in self.files_stats:
                if _item_files_stats:
                    _items.append(_item_files_stats.to_dict())
            _dict['filesStats'] = _items
        # set to None if file_size_distribution (nullable) is None
        # and model_fields_set contains the field
        if self.file_size_distribution is None and "file_size_distribution" in self.model_fields_set:
            _dict['fileSizeDistribution'] = None

        # set to None if files_stats (nullable) is None
        # and model_fields_set contains the field
        if self.files_stats is None and "files_stats" in self.model_fields_set:
            _dict['filesStats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FilesStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fileSizeDistribution": [FileCount.from_dict(_item) for _item in obj["fileSizeDistribution"]] if obj.get("fileSizeDistribution") is not None else None,
            "filesStats": [FilesStatsForEntity.from_dict(_item) for _item in obj["filesStats"]] if obj.get("filesStats") is not None else None
        })
        return _obj


