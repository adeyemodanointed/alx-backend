import { createQueue } from 'kue';

const jobData = {
  phoneNumber: '23470709912',
  message: 'Job Data Message'
};

const queue = createQueue();

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.on('failed', (error) => {
  console.log('Notification job failed');
  throw error;
});
