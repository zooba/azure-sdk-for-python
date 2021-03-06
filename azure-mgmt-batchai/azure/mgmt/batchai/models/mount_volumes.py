# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MountVolumes(Model):
    """Details of volumes to mount on the cluster.

    :param azure_file_shares: Azure File Share setup configuration. References
     to Azure File Shares that are to be mounted to the cluster nodes.
    :type azure_file_shares: list of :class:`AzureFileShareReference
     <azure.mgmt.batchai.models.AzureFileShareReference>`
    :param azure_blob_file_systems: Azure Blob FileSystem setup configuration.
     References to Azure Blob FUSE that are to be mounted to the cluster nodes.
    :type azure_blob_file_systems: list of
     :class:`AzureBlobFileSystemReference
     <azure.mgmt.batchai.models.AzureBlobFileSystemReference>`
    :param file_servers: References to a list of file servers that are mounted
     to the cluster node.
    :type file_servers: list of :class:`FileServerReference
     <azure.mgmt.batchai.models.FileServerReference>`
    :param unmanaged_file_systems: References to a list of file servers that
     are mounted to the cluster node.
    :type unmanaged_file_systems: list of :class:`UnmanagedFileSystemReference
     <azure.mgmt.batchai.models.UnmanagedFileSystemReference>`
    """

    _attribute_map = {
        'azure_file_shares': {'key': 'azureFileShares', 'type': '[AzureFileShareReference]'},
        'azure_blob_file_systems': {'key': 'azureBlobFileSystems', 'type': '[AzureBlobFileSystemReference]'},
        'file_servers': {'key': 'fileServers', 'type': '[FileServerReference]'},
        'unmanaged_file_systems': {'key': 'unmanagedFileSystems', 'type': '[UnmanagedFileSystemReference]'},
    }

    def __init__(self, azure_file_shares=None, azure_blob_file_systems=None, file_servers=None, unmanaged_file_systems=None):
        self.azure_file_shares = azure_file_shares
        self.azure_blob_file_systems = azure_blob_file_systems
        self.file_servers = file_servers
        self.unmanaged_file_systems = unmanaged_file_systems
