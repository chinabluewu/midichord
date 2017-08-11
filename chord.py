
import pretty_midi
import random
# Create the chords:C,Dm,Em,F,G,Am
chordSet1 = [['C3', 'E3', 'G3'], 
            ['D3', 'F3', 'A4'],
            ['E3', 'G3', 'B3'],
            ['F3', 'A3', 'C4'],
            ['G3', 'B3', 'D4'],
            ['A2', 'C3', 'E3']]

#Creat the Cannon chord order	
#chordOrd = [1, 5, 6, 3, 4, 1, 4, 5]
chordOrd = [1, 2,  3, 4, 5, 6]
random.shuffle(chordOrd) 		
print (chordOrd)
	
# Create a PrettyMIDI object
guitar_c_chord = pretty_midi.PrettyMIDI()
# Create an Instrument instance for a cello instrument
guitar_program = pretty_midi.instrument_name_to_program('Acoustic Guitar (nylon)')
#cello_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
guitar = pretty_midi.Instrument(program=guitar_program)

drum = pretty_midi.Instrument(117) #drum

bass = pretty_midi.Instrument(34) #bass

# Iterate over note names, which will be converted to note number later
'''
for note_name in ['C3', 'E3', 'G3']:
    # Retrieve the MIDI note number for this note name
    note_number = pretty_midi.note_name_to_number(note_name)
    # Create a Note instance for this note, starting at 0s and ending at .5s
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=2.0)
    # Add it to our cello instrument
    cello.notes.append(note)
'''
time = 0
for i in chordOrd:
	for note_name in chordSet1[i-1]:
		# Retrieve the MIDI note number for this note name
		note_number = pretty_midi.note_name_to_number(note_name)
		print (note_number)
		# Create a Note instance for this note, starting at 0s and ending at .5s
		note = pretty_midi.Note(velocity=100, pitch=note_number, start=2.0*time, end=2.0*(time+1))
		# Add it to our cello instrument
		guitar.notes.append(note)
	drumNote = pretty_midi.Note(velocity=100, pitch=40, start=2.0*time, end=2.0*(time+0.1))
	drum.notes.append(drumNote)
	
	bassNote_number = pretty_midi.note_name_to_number(chordSet1[i-1][0])-12
	bassNote = pretty_midi.Note(velocity=100, pitch=bassNote_number, start=2.0*time, end=2.0*(time+0.5))
	bass.notes.append(bassNote)
	
	drumNote = pretty_midi.Note(velocity=100, pitch=56, start=2.0*time+1, end=2.0*(time+0.6))
	drum.notes.append(drumNote)
	
	drumNote = pretty_midi.Note(velocity=60, pitch=40, start=2.0*time+1.5, end=2.0*(time+0.8))
	drum.notes.append(drumNote)
    #
	time += 1
	
# Add the cello instrument to the PrettyMIDI object
guitar_c_chord.instruments.append(guitar)
guitar_c_chord.instruments.append(drum)
guitar_c_chord.instruments.append(bass)
# Write out the MIDI data
guitar_c_chord.write('random-C-chord&drum&bass.mid')



