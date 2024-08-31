# Generated by Django 3.1.4 on 2021-01-09 12:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sspanel", "0007_auto_20201122_0831"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NodeOnlineLog",
        ),
        migrations.RemoveField(
            model_name="ssrelayrule",
            name="relay_node",
        ),
        migrations.RemoveField(
            model_name="ssrelayrule",
            name="ss_node",
        ),
        migrations.RemoveField(
            model_name="trojanrelayrule",
            name="relay_node",
        ),
        migrations.RemoveField(
            model_name="trojanrelayrule",
            name="trojan_node",
        ),
        migrations.DeleteModel(
            name="UserOnLineIpLog",
        ),
        migrations.DeleteModel(
            name="UserTrafficLog",
        ),
        migrations.RemoveField(
            model_name="vmessrelayrule",
            name="relay_node",
        ),
        migrations.RemoveField(
            model_name="vmessrelayrule",
            name="vmess_node",
        ),
        migrations.DeleteModel(
            name="RelayNode",
        ),
        migrations.DeleteModel(
            name="SSNode",
        ),
        migrations.DeleteModel(
            name="SSRelayRule",
        ),
        migrations.DeleteModel(
            name="TrojanNode",
        ),
        migrations.DeleteModel(
            name="TrojanRelayRule",
        ),
        migrations.DeleteModel(
            name="VmessNode",
        ),
        migrations.DeleteModel(
            name="VmessRelayRule",
        ),
    ]
