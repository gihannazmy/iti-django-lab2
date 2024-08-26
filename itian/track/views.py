from django.shortcuts import render, redirect

# Simulate a database with a global list of tracks
tracks = [
    {'id': 1, 'name': 'Track 1'},
    {'id': 2, 'name': 'Track 2'},
]

# Custom function to simulate get_object_or_404 for a list
def get_track_or_404(track_list, id):
    for track in track_list:
        if track['id'] == id:
            return track
    return None

def tracks_list(request):
    context = {'tracks': tracks}
    return render(request, 'track/tracksList.html', context)

def track_create(request):
    if request.method == 'POST':
        new_id = len(tracks) + 1
        new_name = request.POST.get('name')

        new_track = {'id': new_id, 'name': new_name}

        tracks.append(new_track)

        return redirect('track_list')
    return render(request, 'track/createTrack.html')

def track_update(request, id):
    track = get_track_or_404(tracks, id)
    if not track:
        return HttpResponse("Track not found", status=404)

    if request.method == 'POST':
        track['name'] = request.POST.get('name')
        return redirect('track_list')
    return render(request, 'track/updateTrack.html', {'track': track})

def track_delete(request, id):
    track = get_track_or_404(tracks, id)
    if not track:
        return HttpResponse("Track not found", status=404)

    if request.method == 'POST':
        tracks.remove(track)
        return redirect('track_list')
    return render(request, 'track/deleteTrack.html', {'track': track})
from django.http import HttpResponse

def track_details(request, id):
    track = get_track_or_404(tracks, id)
    if not track:
        return HttpResponse("Track not found", status=404)

    return render(request, 'track/TrackDetails.html', {'track': track})


