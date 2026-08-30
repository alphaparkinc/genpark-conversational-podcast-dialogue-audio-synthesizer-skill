from client import ConversationalPodcastDialogueAudioSynthesizerClient

def main():
    client = ConversationalPodcastDialogueAudioSynthesizerClient()
    res = client.synthesize_podcast_episode('Deep dive into neuromorphic computing and memristor arrays', 2, 8)
    print('Podcast Synthesizer: ' + res['podcast_generation_id'] + ' (' + str(res['dialogue_turns_count']) + ' dialogue turns)')
    print('Natural Cues & Inflections: ' + str(res['interrupted_laughter_cues_synthesized']) + ' | Prosody: ' + str(res['bilingual_prosody_score_pct']) + '%')
    print('Mastered Audio: ' + res['mastered_audio_mp3_url'])

if __name__ == '__main__':
    main()
