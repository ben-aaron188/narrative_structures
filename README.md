# Identifying the narrative styles of YouTube’s vloggers

Data and code for the paper "B. Kleinberg, M. Mozes and I. van der Vegt, 2018. [Identifying the sentiment styles of YouTube’s vloggers](https://arxiv.org/abs/1808.09722). To appear in Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), Brussels, Belgium, 2018". 

The downloaded  YouTube transcripts can be found in the `data/output_dir` directory. We provide the transcripts come in two different ways:

* *raw* (`data/output_dir/raw`): contains the raw and XML-encoded transcripts for each video as .txt file including temporal information about the start and end date at which a sequence is visible to the viewer when plaing a video.
* *parsed* (`data/output_dir/parsed`): contains the parsed transcripts for each video, i.e. a continuous text  consisting of the concatenation of all sequences for a video. 

We provide metadata information for each video in `data/overview.txt`. This file contains comma-separated metadata for one video in each row. The first two elements of each row uniquely define the transcript file (vlogger name + local id). For example, the transcript file for *Bratayley,1* would be the file `1.txt` in `data/output_dir/[raw/parsed]/Bratayley`. In total, the information in each row represent *username of vlogger, local id, video url, view count, date of video publication, url to user's YouTube channel*.

