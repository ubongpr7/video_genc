# Generated by Django 4.2.16 on 2024-10-26 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapps.vidoe_text.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AudioClip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("audio_file", models.FileField(upload_to="audio_clips/")),
                ("duration", models.FloatField(blank=True, null=True)),
                ("voice_id", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="LogoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("logo", models.FileField(upload_to="logos/")),
            ],
        ),
        migrations.CreateModel(
            name="TextFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=mainapps.vidoe_text.models.text_file_upload_path,
                    ),
                ),
                ("voice_id", models.CharField(max_length=100)),
                ("processed", models.BooleanField(default=False)),
                ("progress", models.CharField(default="0", max_length=100)),
                ("api_key", models.CharField(max_length=200)),
                ("resolution", models.CharField(max_length=50)),
                (
                    "font_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=mainapps.vidoe_text.models.font_file_upload_path,
                    ),
                ),
                (
                    "bg_level",
                    models.DecimalField(
                        blank=True,
                        decimal_places=9,
                        default=0.1,
                        max_digits=12,
                        null=True,
                    ),
                ),
                ("font", models.CharField(default="Arial", max_length=50)),
                ("font_color", models.CharField(max_length=7)),
                (
                    "subtitle_box_color",
                    models.CharField(blank=True, max_length=7, null=True),
                ),
                ("font_size", models.IntegerField()),
                (
                    "bg_music_text",
                    models.FileField(
                        blank=True, null=True, upload_to="background_txt/"
                    ),
                ),
                ("fps", models.IntegerField(default=30, editable=False)),
                (
                    "audio_file",
                    models.FileField(blank=True, null=True, upload_to="audio_files"),
                ),
                (
                    "srt_file",
                    models.FileField(blank=True, null=True, upload_to="srt_files/"),
                ),
                (
                    "blank_video",
                    models.FileField(blank=True, null=True, upload_to="blank_video/"),
                ),
                (
                    "subtitle_file",
                    models.FileField(blank=True, null=True, upload_to="subtitles/"),
                ),
                (
                    "generated_audio",
                    models.FileField(
                        blank=True, null=True, upload_to="generated_audio/"
                    ),
                ),
                (
                    "generated_srt",
                    models.FileField(blank=True, null=True, upload_to="generated_srt/"),
                ),
                (
                    "generated_blank_video",
                    models.FileField(
                        blank=True, null=True, upload_to="generated_blank_video/"
                    ),
                ),
                (
                    "generated_final_video",
                    models.FileField(
                        blank=True, null=True, upload_to="generated_final_video/"
                    ),
                ),
                (
                    "generated_watermarked_video",
                    models.FileField(
                        blank=True, null=True, upload_to="generated_watermarked_video/"
                    ),
                ),
                (
                    "generated_final_bgm_video",
                    models.FileField(
                        blank=True, null=True, upload_to="generated_bgm_video/"
                    ),
                ),
                (
                    "generated_final_bgmw_video",
                    models.FileField(
                        blank=True, null=True, upload_to="generated_bgmw_video/"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TextLineVideoClip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "video_file_path",
                    models.FileField(
                        upload_to=mainapps.vidoe_text.models.text_clip_upload_path
                    ),
                ),
                ("line_number", models.IntegerField()),
                ("timestamp_start", models.FloatField(blank=True, null=True)),
                ("timestamp_end", models.FloatField(blank=True, null=True)),
                (
                    "text_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_clips",
                        to="vidoe_text.textfile",
                    ),
                ),
                (
                    "video_file",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="usage",
                        to="video.videoclip",
                    ),
                ),
            ],
            options={
                "ordering": ["line_number", "text_file"],
                "unique_together": {("text_file", "line_number")},
            },
        ),
    ]
